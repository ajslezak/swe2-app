from django.contrib import admin

# Register your models here.
from .models import Question, Choice
#admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)