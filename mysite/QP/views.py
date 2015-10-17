from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from QP.models import Question
from django.http import HttpResponse
 
def index(request):
	template=get_template('QP/j.html')
	variables = Context({
				 'Question_list' : Question.objects.all(),
				})
	output=template.render(variables)
	return HttpResponse(output)