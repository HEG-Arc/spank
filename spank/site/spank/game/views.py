from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext, loader
from .models import Poll, Choice, User, UserForm, Answer, Visit, Friend
import datetime


def permissions(request):
    if request.method == 'POST':
        # Initialization of the session in order to have a session_key
        request.session['start'] = request.POST['start']
    template = loader.get_template('game/permissions.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def intro(request):
    return render_to_response('game/intro.html', {
        #
    }, context_instance=RequestContext(request))


def pageperm(request):

    if request.method == 'POST':
        request.session['permissions'] = request.POST['permissions']
        visit = Visit()
        visit.auth_accepted = request.session['permissions']
        visit.session_number = request.session.session_key
        visit.save()
        return HttpResponseRedirect('page1')
    return HttpResponseRedirect('permissions')


def create(request):
    form = UserForm()
    template = loader.get_template('game/create.html')
    context = RequestContext(request, {
        'form': form,
    })
    return HttpResponse(template.render(context))


def edit(request, number_id):
    user = User.objects.get(pk=number_id)
    if user.number == request.session['spank_user'].number:
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
            request.session['spank_user'] = new_user
            template = loader.get_template('game/thanks.html')
            context = RequestContext(request, {
                'new_user': new_user,
            })
            return HttpResponse(template.render(context))
    else:
        raise Http404


def question1(request):
    poll = Poll.objects.get(template='question', sequence=1)
    try:
        answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
        choice = answer.choice.number
    except Answer.DoesNotExist:
        choice = 1
    template = loader.get_template('game/question1.html')
    context = RequestContext(request, {
        'poll': poll,
        'choice': choice,
    })
    return HttpResponse(template.render(context))


def page12(request):
    poll = Poll.objects.get(template='question', sequence=1)
    if request.method == 'POST':
        p = request.POST
        if "answer" in p:
            try:
                answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
                answer.choice = Choice.objects.get(number=p['answer'])
            except Answer.DoesNotExist:
                answer = Answer(user=request.session['spank_user'], poll=poll, choice=Choice.objects.get(number=p['answer']))
            answer.save()
    template = loader.get_template('game/12.html')
    context = RequestContext(request, {
        'poll': poll,
    })
    return HttpResponse(template.render(context))


def question2(request):
    poll = Poll.objects.get(template='question', sequence=2)
    try:
        answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
        choice = answer.choice.number
    except Answer.DoesNotExist:
        choice = 1
    template = loader.get_template('game/question2.html')
    context = RequestContext(request, {
        'poll': poll,
        'choice': choice,
    })
    return HttpResponse(template.render(context))


def page13(request):
    poll = Poll.objects.get(template='question', sequence=2)
    if request.method == 'POST':
        p = request.POST
        if "answer" in p:
            try:
                answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
                answer.choice = Choice.objects.get(number=p['answer'])
            except Answer.DoesNotExist:
                answer = Answer(user=request.session['spank_user'], poll=poll, choice=Choice.objects.get(number=p['answer']))
            answer.save()
    template = loader.get_template('game/13.html')
    context = RequestContext(request, {
        'poll': poll,
    })
    return HttpResponse(template.render(context))


def question3(request):
    poll = Poll.objects.get(template='question', sequence=3)
    try:
        answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
        choice = answer.choice.number
    except Answer.DoesNotExist:
        choice = 1
    template = loader.get_template('game/question3.html')
    context = RequestContext(request, {
        'poll': poll,
        'choice': choice,
    })
    return HttpResponse(template.render(context))


def page14(request):
    poll = Poll.objects.get(template='question', sequence=3)
    if request.method == 'POST':
        p = request.POST
        if "answer" in p:
            try:
                answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
                answer.choice = Choice.objects.get(number=p['answer'])
            except Answer.DoesNotExist:
                answer = Answer(user=request.session['spank_user'], poll=poll, choice=Choice.objects.get(number=p['answer']))
            answer.save()
    template = loader.get_template('game/14.html')
    context = RequestContext(request, {
        'poll': poll,
    })
    return HttpResponse(template.render(context))


def chart(request):
    chiara = Answer.objects.get(user_id=request.session['spank_user'].id, poll_id=1)
    simone = Answer.objects.get(user_id=request.session['spank_user'].id, poll_id=2)
    richard = Answer.objects.get(user_id=request.session['spank_user'].id, poll_id=3)
    template = loader.get_template('game/chart.html')
    context = RequestContext(request, {
        'chiaragreen': range(int(chiara.choice_id)),
        'chiara': range(int(5 - chiara.choice_id)),
        'simonegreen': range(int(simone.choice_id)),
        'simone': range(int(5 - simone.choice_id)),
        'richardgreen': range(int(richard.choice_id)),
        'richard': range(int(5 - richard.choice_id)),
    })
    return HttpResponse(template.render(context))


def chart2(request):
    chiara = Answer.objects.get(user_id=request.session['spank_user'].id, poll_id=1)
    simone = Answer.objects.get(user_id=request.session['spank_user'].id, poll_id=2)
    richard = Answer.objects.get(user_id=request.session['spank_user'].id, poll_id=3)
    template = loader.get_template('game/chart2.html')
    context = RequestContext(request, {
        'chiaragreen': range(int(chiara.choice_id)),
        'chiara': range(int(5 - chiara.choice_id)),
        'simonegreen': range(int(simone.choice_id)),
        'simone': range(int(5 - simone.choice_id)),
        'richardgreen': range(int(richard.choice_id)),
        'richard': range(int(5 - richard.choice_id)),
    })
    return HttpResponse(template.render(context))


def privacy1(request):
    poll = Poll.objects.filter(template='privacy1').order_by('sequence')[0]
    try:
        answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
        choice = answer.choice.number
    except Answer.DoesNotExist:
        choice = 1
    if request.method == 'POST':
        p = request.POST
        poll = Poll.objects.filter(sequence=p['sequence'], template='privacy1')[0]
        if p.has_key("answer"):
            try:
                answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
                answer.choice = Choice.objects.get(number=p['answer'])
            except Answer.DoesNotExist:
                answer = Answer(user=request.session['spank_user'], poll=poll, choice=Choice.objects.get(number=p['answer']))
            answer.save()
        if p.has_key("next"):
            sequence = p['next']
            poll = Poll.objects.filter(sequence=sequence, template='privacy1')[0]
        else:
            return redirect('/game/page18')

    template = loader.get_template('game/question.html')
    context = RequestContext(request, {
        'poll': poll,
        'choice': choice,
    })
    return HttpResponse(template.render(context))


def privacy2(request):
    poll = Poll.objects.filter(template='privacy2').order_by('sequence')[0]
    try:
        answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
        choice = answer.choice.number
    except Answer.DoesNotExist:
        choice = 1
    if request.method == 'POST':
        p = request.POST
        poll = Poll.objects.filter(sequence=p['sequence'], template='privacy2')[0]
        if p.has_key("answer"):
            try:
                answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
                answer.choice = Choice.objects.get(number=p['answer'])
            except Answer.DoesNotExist:
                answer = Answer(user=request.session['spank_user'], poll=poll, choice=Choice.objects.get(number=p['answer']))
            answer.save()
        if p.has_key("next"):
            sequence = p['next']
            poll = Poll.objects.filter(sequence=sequence, template='privacy2')[0]
        else:
            return redirect('/game/page22')

    template = loader.get_template('game/question.html')
    context = RequestContext(request, {
        'poll': poll,
        'choice': choice,
    })
    return HttpResponse(template.render(context))


def multiply(request, factor_id):
    template = loader.get_template('game/multiply.html')
    context = RequestContext(request, {
        'factor': range(int(factor_id)),
        'factor_id': factor_id,
    })
    return HttpResponse(template.render(context))


def bye(request):
    if request.method == 'POST':
        p = request.POST
        for i in range(int(p['factor'])):
            friend = Friend()
            friend.email = p['email_' + str(i)]
            friend.user = request.session['spank_user']
            friend.save()

    template = loader.get_template('game/bye.html')
    context = RequestContext(request, {
        'player': request.session['spank_user'],
    })
    return HttpResponse(template.render(context))


def culprit(request, name=None):
    if name:
        if name == "Chiara":
            culprit_name = "Chiara"
        elif name == "Simone":
            culprit_name = "Simone"
        elif name == "Richard":
            culprit_name = "Richard"
        elif name == "Autre":
            culprit_name = "Autre"
    user = request.session['spank_user']
    user.coupable = culprit_name
    user.last_update_at = datetime.datetime.now()
    user.save()
    request.session['spank_user'] = user

    nb_chiara = User.objects.filter(coupable='Chiara').count()
    nb_simone = User.objects.filter(coupable='Simone').count()
    nb_richard = User.objects.filter(coupable='Richard').count()
    nb_autre = User.objects.filter(coupable='Autre').count()
    nb_total = nb_chiara + nb_simone + nb_richard + nb_autre

    prct_chiara = 100*nb_chiara/nb_total
    prct_simone = 100*nb_simone/nb_total
    prct_richard = 100*nb_richard/nb_total
    prct_autre = 100*nb_autre/nb_total


    return render_to_response('game/23.html', {
        'culprit': culprit_name,
        'nb_chiara': prct_chiara,
        'nb_simone': prct_simone,
        'nb_richard': prct_richard,
        'nb_autre': prct_autre,

    }, context_instance=RequestContext(request))


def page24(request, accept):
    user = request.session['spank_user']
    user.contact_access = accept
    user.save()
    request.session['spank_user'] = user
    template = loader.get_template('game/24.html')
    context = RequestContext(request, {
        'accept': accept,
    })
    return HttpResponse(template.render(context))


def gipc_question(request, sequence):
    sequence = int(sequence)
    poll = Poll.objects.get(template='gipc', sequence=sequence)
    try:
        answer = Answer.objects.get(user=request.session['spank_user'], poll=poll)
        choice = answer.choice.number
    except Answer.DoesNotExist:
        choice = 1
    if request.method == 'POST':
        p = request.POST
        save_poll = Poll.objects.get(sequence=p['sequence'], template='gipc')
        if "answer" in p:
            try:
                answer = Answer.objects.get(user=request.session['spank_user'], poll=save_poll)
                answer.choice = Choice.objects.get(number=p['answer'])
            except Answer.DoesNotExist:
                answer = Answer(user=request.session['spank_user'], poll=save_poll, choice=Choice.objects.get(number=p['answer']))
            answer.save()

    if sequence < 4:
        return render_to_response('game/gipc-q.html', {
            'poll': poll,
            'choice': choice,
        }, context_instance=RequestContext(request))
    else:
        return redirect('/game/page8')
