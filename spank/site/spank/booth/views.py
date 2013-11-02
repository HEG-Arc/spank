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

# Core Django imports
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist

# Third-party app imports

# Appagoo imports
from game.models import User, Answer


class ScanQRForm(forms.Form):
    scanqr = forms.CharField()


#@login_required()
def adscreen(request):
    #hire = get_object_or_404(Hire, pk=hire_id)
    return render_to_response('booth/adscreen.html', {
        #'hire': hire,
    }, context_instance=RequestContext(request))


#@login_required()
def scanqr(request):
    if request.method == 'POST':
        form = ScanQRForm(request.POST)
        if form.is_valid():
            qr = form.cleaned_data['scanqr']
            try:
                player = User.objects.get(pk=qr)
            except ObjectDoesNotExist:
                messages.error(request, _(u"Le QR-Code ne correspond pas à un détective!"))
                return HttpResponseRedirect(reverse('booth-adscreen'))
            except ValueError:
                messages.error(request, _(u"Le QR-Code scanné n'est pas dans un format reconnu!"))
                return HttpResponseRedirect(reverse('booth-adscreen'))
            if player.prize:
                return HttpResponseRedirect(reverse('booth-cheater', args=(player.id,)))
            else:
                return HttpResponseRedirect(reverse('booth-summary', args=(player.id,)))
        else:
            messages.error(request, _(u"Je n'ai pas pu lire le QR-Code que vous avez scanné...!"))
    else:
        messages.error(request, _(u"Aucun QR-Code scanné!"))
    return HttpResponseRedirect(reverse('booth-adscreen'))


def summary(request, user_id):
    player = get_object_or_404(User, pk=user_id)

    chiara = Answer.objects.get(user_id=player.id, poll_id=1)
    simone = Answer.objects.get(user_id=player.id, poll_id=2)
    richard = Answer.objects.get(user_id=player.id, poll_id=3)
    return render_to_response('booth/summary.html', {
        'player': player,
        'chiaragreen': range(int(chiara.choice_id)),
        'chiara': range(int(5-chiara.choice_id)),
        'simonegreen': range(int(simone.choice_id)),
        'simone': range(int(5-simone.choice_id)),
        'richardgreen': range(int(richard.choice_id)),
        'richard': range(int(5-richard.choice_id)),
    }, context_instance=RequestContext(request))


def prize(request, user_id):
    player = get_object_or_404(User, pk=user_id)
    return render_to_response('booth/prize.html', {
        'player': player,
    }, context_instance=RequestContext(request))


def cheater(request, user_id):
    player = get_object_or_404(User, pk=user_id)
    return render_to_response('booth/cheater.html', {
        'player': player,
    }, context_instance=RequestContext(request))