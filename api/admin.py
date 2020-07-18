from django.contrib import admin
from .models import Question, Subject, Option
# Register your models here.

admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Option)
