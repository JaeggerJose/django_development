from dataclasses import field
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline): #TabularInline and StackedInline two different to render this div for website.
    model = Choice # model for this StackedInline
    extra = 5 #number of  extra choice will be show on the website.

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] # redefine the file render methode
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date informaton', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')




admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question)
admin.site.register(Choice)