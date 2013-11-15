from django.contrib import admin
from .models import Poll, Choice, Answer, Friend, Visit

admin.site.register(Visit)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Friend)