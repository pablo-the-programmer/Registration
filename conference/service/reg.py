# -*- coding: utf-8 -*-


from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponseRedirect


from service.models import Event
from service.models import Domain
from service.models import Registration
from service.forms import RegistrationForm
from service.models import Question, RQLink


def register(request, event_id):
    template = loader.get_template('service/register.html')
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['name']
            flast_name = form.cleaned_data['last_name']
            femail = form.cleaned_data['contact_email']
            fphone = form.cleaned_data['contact_phone']
            q = Registration(event = Event.objects.get(pk = event_id),
                             name = fname,
                             last_name = flast_name,
                             contact_email = femail,
                             contact_phone = fphone)
            q.save()
            for field in request.POST.keys():
                if not field.startswith('cq_'):
                    continue
                q_id = field[3:]
                v = request.POST[field]
                if len(v) == 0:
                    continue
                a = RQLink()
                a.registration = q
                a.question = Question.objects.get(pk = q_id)
                a.answer = v
                a.save()
                q.rqlink_set.add(a)
            
            q.save()
            #tutaj wysyłamy maila z potwierdzeniem
    else:
        form = RegistrationForm()
     
    event = Event.objects.get(pk = event_id)
    ql = []
    for q in event.eqlink_set.all():
        ql.append({'id':q.id,'q':q.question.text,'required':q.required})
    return render(request, 'service/register.html', {
        'form': form,
        'question_list' : ql,
        'event' : event
            })


def update(request, reg_uuid):
    user = Registration.objects.get(uuid = reg_uuid)
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['name']
            flast_name = form.cleaned_data['last_name']
            femail = form.cleaned_data['contact_email']
            fphone = form.cleaned_data['contact_phone']
            q = Registration(event_name = Event.objects.get(pk = event_id),
                             name = fname,
                             last_name = flast_name,
                             contact_email = femail,
                             contact_phone = fphone)
            q.save()
            #tutaj wysyłamy maila z potwierdzeniem
    else:
        user_data = {}
        user_data['name'] = user.name
        user_data['last_name'] = user.last_name
        user_data['contact_email'] = user.contact_email
        user_data['contact_phone'] = user.contact_phone
        form = RegistrationForm(user_data)
    event = Event.objects.get(pk = user.event.id)
    
    ql = []
    for q in user.rqlink_set.all():
        ql.append({'id':q.question.id,'q':q.question.text,'required':event.eqlink_set.get(question_id = q.question.id).required,'value':q.answer})

    return render(request, 'service/update.html',{
        'form':form,   
        'user': user,
        'question_list':ql
    })


def update_by_id(request, reg_id):
    r = Registration.objects.get(pk = reg_id)
    return update(request, r.uuid)

