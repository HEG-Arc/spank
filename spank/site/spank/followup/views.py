# -*- coding: UTF-8 -*-
# views.py
#
# Copyright (C) 2013 HES-SO//HEG Arc
#
# Author(s): Cédric Gaspoz <cedric.gaspoz@he-arc.ch>
#
# This file is part of appagoo.
#
# appagoo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# appagoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with appagoo.  If not, see <http://www.gnu.org/licenses/>.

# Stdlib imports
from random import randrange
import logging

# Core Django imports
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Third-party app imports
from faker import Factory

# Appagoo imports
from game.models import User
from .models import Registration
from spank import settings

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UserModelField(forms.IntegerField):

    def to_python(self, value):
        pk = super(UserModelField, self).to_python(value)

        if pk is None:
            raise ValidationError(_('Invalid id %(pk)s' % {'pk': pk}))

        try:
            obj = User.objects.get(id=pk)
        except ObjectDoesNotExist, e:
            raise ValidationError(_('There is no User object with id %(pk)d %(value)s: %(e)s') %
                                   {'pk': pk, 'value': value, 'e': e})
        except MultipleObjectsReturned, e:
            raise ValidationError(_('Multiple User objects have id %(id)d: %(e)s') % {'id': pk, 'e': e})

        return obj


class TriggerMailForm(forms.Form):
    action = forms.BooleanField(required=False)
    sid = UserModelField(widget=forms.HiddenInput)
    model_obj = None

    def __init__(self, *args, **kwargs):
        super(TriggerMailForm, self).__init__(*args, **kwargs)
        if not self.is_bound:
            if 'model' in self.initial:
                self.model_obj = self.initial['model']
        #else:
        #    raise ValidationError(_('This form must be initialized with a model instance.'))

    def clean_sid(self):
        self.model_obj = self.cleaned_data['sid']

        return self.cleaned_data['sid']

TriggerMailFormset = forms.formsets.formset_factory(TriggerMailForm, extra=0)


class AnonymizeForm(forms.Form):
    register = forms.BooleanField(initial=True, label=_(u"Gardez mon adresse e-mail pour m'informer des résultats de ce projet"))


def index(request):
    return render_to_response('followup/index.html', {
        #'hire': hire,
    }, context_instance=RequestContext(request))


def result(request, number):
    player = get_object_or_404(User, number=number)
    form = AnonymizeForm()
    return render_to_response('followup/result.html', {
        'player': player,
        'form': form,
    }, context_instance=RequestContext(request))


def anonymize(request, player_id):
    player = get_object_or_404(User, pk=player_id)
    if request.method == 'POST':
        fake = Factory.create('fr_FR')
        form = AnonymizeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['register'] == True:
                registration = Registration()
                registration.email = player.email
                registration.save()
            player.firstname = fake.first_name()
            player.lastname = fake.last_name()
            player.email = fake.company_email()
            player.register = form.cleaned_data['register']
            player.save()
    else:
        return HttpResponseRedirect(reverse('fup-result', args=(player.number,)))

    return render_to_response('followup/anonymize.html', {
        'player': player,
    }, context_instance=RequestContext(request))


def create_email(user):
    template_html = 'followup/newsletter.html'
    template_text = 'followup/newsletter.txt'
    to = user.email
    from_email = settings.DEFAULT_FROM_EMAIL
    subject = _(u"[HE-Arc] Détective Spank")

    text_content = render_to_string(template_text, {"number": user.number})
    html_content = render_to_string(template_html, {"number": user.number})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")

    return msg


def send_emails(selected_players):
    from django.core.mail import get_connection, EmailMultiAlternatives

    connection = get_connection() # uses SMTP server specified in settings.py
    connection.open() # If you don't open the connection manually, Django will automatically open, then tear down the connection in msg.send()

    for user in selected_players:
        #try:
            msg = create_email(user)
            msg.send()
            user.notified = True
        #except:
        #    pass

    connection.close()


@login_required()
def mailing(request):
    logger.debug("mailing call")
    if 'POST' == request.method:
        selected_players = []
        formset = TriggerMailFormset(request.REQUEST)

        if formset.is_valid():   # run the validations
            for form in formset:
                if form.cleaned_data['action']:
                    player = form.cleaned_data['sid']
                    selected_players.append(player)
                    # Send the email...
                    logger.debug("Selected players", selected_players)
            send_emails(selected_players)
            return HttpResponseRedirect(reverse('fup-mailing'))
        else:
            # if we have only chosen valid forms, go ahead and process the formset
            # this allows us to unselect the invalid forms and resubmit
            process = True

            # if there are any selected invalid forms, do not process any valid forms
            for form in formset:
                if not form.is_valid():
                    # test if action was selected.  Hmm.
                    if form['action'].value():
                        process = False

            if process:
                for form in formset:
                    if form.is_valid() and form.cleaned_data['action']:
                        player = form.cleaned_data['sid']
                        selected_players.append(player)
                        logger.debug("Selected players", selected_players)
                        # Send the email...
                send_emails(selected_players)
                return HttpResponseRedirect(reverse('fup-mailing'))
    else:
        users_list = []
        users = User.objects.exclude(last_update_at__isnull=True).exclude(email__exact='').exclude(notified__exact=True)
        for user in users:
            data = {}
            data['sid'] = user.id
            data['model'] = user
            users_list.append(data)

        formset = TriggerMailFormset(initial=users_list)

    return render_to_response('followup/mailing.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))


