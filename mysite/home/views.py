from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context 
from django.http import HttpResponse
from junior.models import details
def index(request):
	template=get_template('home/index.html')
	variables=Context({
				'user_name':details.Name,
				'registration_no':details.RegNo,
				'user-phoneno':details.PhoneNo,
				'school':details.School,
		})
	output=template.render(variables)
	return HttpResponse(output)
def login(request,template='index.html'):
	return HttpResponseRedirect('/junior/')
