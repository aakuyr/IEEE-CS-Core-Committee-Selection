from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))
#from django.http import HttpResponse
#def index(request):
#	return HttpResponse("Hello!")
def login(request,template='index.html'):
	return HttpResponseRedirect('/junior/')
