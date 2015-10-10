from django.db import models

# Create your models here.
class Question(models.Model):
	question_text=models.TextField()
	def __unicode__(self):
		return self.question_text
class Answer(models.Model):
	question=models.ForeignKey(Question)
	ANSWER_CHOICES=(
		('1','One'),
		('2','Two'),
		('3','Three'),
		('4','Four') ,
	)
	answer_text=models.CharField(max_length=1,choices=ANSWER_CHOICES)