from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('home.html', { "this": "this"}, context_instance=RequestContext(request))