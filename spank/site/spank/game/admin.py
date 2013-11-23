from django.contrib import admin
from .models import Poll, Choice, Answer, Friend, Visit, User



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'auth_accepted', 'email', 'coupable', 'created_at', 'updated_at')
    list_filter = ('created_at', )


admin.site.register(User, UserAdmin)

admin.site.register(Visit)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Friend)
