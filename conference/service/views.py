# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponseRedirect


from service.models import Event
from service.models import Domain


def index(request):
        domain_name = request.META['HTTP_HOST'].split(":",1)[0] 
        domain_obj = Domain.objects.get(name = domain_name)
        events = domain_obj.events.all()
        template = loader.get_template('service/index.html')
        context = RequestContext(request, {
            'events': events,
            'domain' : domain_obj
        })
        return HttpResponse(template.render(context))


def events(request, event_id):
        event = Event.objects.get(pk = event_id)
        template = loader.get_template('service/event.html')
        context = RequestContext(request, {
            'event': event,
            'host': request.META,
        }) 
        return HttpResponse(template.render(context))
