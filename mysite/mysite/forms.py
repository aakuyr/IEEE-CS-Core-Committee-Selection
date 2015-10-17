from django import forms
from django.forms.widgets import RadioSelect
from QP.models import Answer,Question
class Questions(forms.ModelForm):
	class Meta:
		question_list=Question.objects.all()
		model=Question