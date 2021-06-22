from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from mytutor.models import Tutor, Question

# Register your models here.
class TutorAdmin(ModelAdmin):
    list_display = ["name", "subject"]
    search_fields = ["name", "subject"]
admin.site.register(Tutor, TutorAdmin)

class QuestionAdmin(ModelAdmin):
    list_display = ["question","cr_date"]
    search_fields = ["question"]
admin.site.register(Question, QuestionAdmin)
