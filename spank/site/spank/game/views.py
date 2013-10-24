from django.contrib.redirects.models import Redirect
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from game.models import Poll, Choice, User, UserForm, Answer


def page1(request):
    if request.method == 'POST':
        request.session['permissions'] = request.POST['permissions']
    else:
        request.session['permissions'] = "accepted"

    template = loader.get_template('game/1.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def create(request):
    form = UserForm()
    template = loader.get_template('game/create.html')
    context = RequestContext(request, {
        'form': form,
    })
    return HttpResponse(template.render(context))


def edit(request, number_id):
    user = User.objects.get(pk=number_id)
    if user.number == request.session['user'].number:
        form = UserForm(instance=user)
        template = loader.get_template('game/edit.html')
        context = RequestContext(request, {
            'form': form,
        })
        return HttpResponse(template.render(context))
    else:
        raise Http404


def thanks(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.number = request.session.session_key
            new_user.auth_accepted = request.session['permissions']
            new_user.save()
            request.session['user'] = new_user
            template = loader.get_template('game/thanks.html')
            context = RequestContext(request, {
                'new_user': new_user,
            })
            return HttpResponse(template.render(context))
    else:
        raise Http404


def questions(request):
    poll = Poll.objects.order_by('sequence')[0]
    if request.method == 'POST':
        p = request.POST
        if p.has_key("answer"):
            answer = Answer(user=request.session['user'], poll=poll, choice=Choice.objects.filter(number=p["answer"])[0])
            answer.save()
        if p.has_key("sequence"):
            sequence = p['sequence']
            poll = Poll.objects.filter(sequence=sequence)[0]
        else:
            return redirect('/game/process')

    template = loader.get_template('game/question_big.html')
    context = RequestContext(request, {
        'poll': poll,
    })
    return HttpResponse(template.render(context))


def multiply(request, factor_id):
    template = loader.get_template('game/multiply.html')
    context = RequestContext(request, {
        'factor': range(int(factor_id)),
    })
    return HttpResponse(template.render(context))
