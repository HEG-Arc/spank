from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["number", "created_at"]