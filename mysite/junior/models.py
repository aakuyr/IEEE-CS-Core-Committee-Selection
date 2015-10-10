from django.db import models
from QP.models import Answer
from QP.models import Question
# Create your models here.
class details(models.Model):
	RegNo=models.CharField(max_length=9)
	Name=models.CharField(max_length=100)
	PhoneNo=models.IntegerField()
	School=models.CharField(max_length=7)
class answers(models.Model):
	answers_option=models.IntegerField()
class questions(models.Model):
	question1=models.ForeignKey(Question)
