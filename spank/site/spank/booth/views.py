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

# Core Django imports
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist


# Third-party app imports

# Appagoo imports
from game.models import User, Answer
from .models import Prize


class ScanQRForm(forms.Form):
    scanqr = forms.CharField()


class PrizeForm(forms.Form):
    prize = forms.IntegerField()


@login_required()
def adscreen(request):
    #hire = get_object_or_404(Hire, pk=hire_id)
    return render_to_response('booth/adscreen.html', {
        #'hire': hire,
    }, context_instance=RequestContext(request))


@login_required()
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
            if player.id == 83:
                return HttpResponseRedirect(reverse('booth-prize', args=(player.id,)))
            if player.prize:
                return HttpResponseRedirect(reverse('booth-cheater', args=(player.id,)))
            else:
                return HttpResponseRedirect(reverse('booth-summary', args=(player.id,)))
        else:
            messages.error(request, _(u"Je n'ai pas pu lire le QR-Code que vous avez scanné...!"))
    else:
        messages.error(request, _(u"Aucun QR-Code scanné!"))
    return HttpResponseRedirect(reverse('booth-adscreen'))


@login_required()
def summary(request, user_id):
    player = get_object_or_404(User, pk=user_id)

    chiara = Answer.objects.get(user_id=player.id, poll_id=1)
    simone = Answer.objects.get(user_id=player.id, poll_id=2)
    richard = Answer.objects.get(user_id=player.id, poll_id=3)
    return render_to_response('booth/summary.html', {
        'player': player,
        'chiarared': int(chiara.choice_id*55.6),
        'simonered': int(simone.choice_id*55.6),
        'richardred': int(richard.choice_id*55.6),
    }, context_instance=RequestContext(request))


@login_required()
def prize(request, user_id):
    player = get_object_or_404(User, pk=user_id)
    past_prize = int(request.session.get('prize', 12))
    print "Past_prize: %s" % past_prize
    random_prize = get_random_prize(past_prize)
    player.prize = random_prize
    player.save()
    request.session['prize'] = random_prize.id
    return render_to_response('booth/prize.html', {
        'player': player,
        'prize': random_prize,
    }, context_instance=RequestContext(request))


@login_required()
def cheater(request, user_id):
    player = get_object_or_404(User, pk=user_id)
    return render_to_response('booth/cheater.html', {
        'player': player,
    }, context_instance=RequestContext(request))


def get_random_prize(past_prize):
    prizes_list = Prize.objects.all().filter(stock__gt=0)
    # We build a dict with all available prizes
    prizes_dict = {}
    total_percent = 0
    for prize in prizes_list:
        prizes_dict[prize.id] = prize.percentage
        if prize.percentage != 100:
            total_percent += prize.percentage
    # We build a list with all prizes
    weighted_prizes_list = []
    for p in prizes_dict:
        if prizes_dict[p] != 100:
            for i in range(0, prizes_dict[p]):
                weighted_prizes_list.append(p)
        else:
            for i in range(0, 100-total_percent):
                weighted_prizes_list.append(p)
    # We randomly choose one prize in the list
    prize = weighted_prizes_list[randrange(len(weighted_prizes_list))]
    print "Random prize: %s" % prize
    while prize == past_prize:
        prize = weighted_prizes_list[randrange(len(weighted_prizes_list))]
        print "Random prize: %s" % prize
    random_prize = get_object_or_404(Prize, pk=prize)
    chng_stock_prize = Prize.objects.get(pk=prize)
    chng_stock_prize.stock -= 1
    chng_stock_prize.save()
    return random_prize