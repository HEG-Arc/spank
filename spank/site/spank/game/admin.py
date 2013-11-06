from django.contrib import admin
from .models import Poll, Choice, Answer

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)