from django.contrib import admin

from polls.models import Choice, Question, Chinko

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Chinko)
