from django import forms
from django.forms.widgets import RadioSelect
from QP.models import Answer
class Questions(forms.ModelForm):
	class Meta:
		model=Answer
		widgets={'type': forms.RadioSelect}