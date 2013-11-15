from django.contrib import admin
from .models import Poll, Choice, Answer, Friend, Visit, User

admin.site.register(Visit)
admin.site.register(User)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Friend)