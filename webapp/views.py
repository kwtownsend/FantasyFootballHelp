from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.



def handler404(request):
    response = render_to_response('help_app/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('help_app/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
