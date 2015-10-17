from django.contrib import admin
from .models import Question,Answer
# Register your models here.
class AnswerInLine(admin.TabularInline):
	model=Answer
	extra=0
class QuestionAdmin(admin.ModelAdmin):
	fieldsets= [
	('Question',{'fields':['question_text']}),
	]
	inlines=[AnswerInLine]
admin.site.register(Question,QuestionAdmin)