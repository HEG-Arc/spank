# coding=utf-8
from django.db import models
from django import forms
from django.forms import TextInput, Select


class Visit(models.Model):
    session_number = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    R = " "
    F = "F"
    M = "M"
    GENDERS = ((R, "Sexe"), (F, "Féminin"), (M, "Masculin"))
    number = models.CharField(max_length=500, blank=True, null=True)
    auth_accepted = models.CharField(max_length=500, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    locality = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=R)
    height = models.CharField(max_length=5, blank=True, null=True)
    weight = models.CharField(max_length=5, blank=True, null=True)
    distinctive_signs = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/game/qrcode/%i/" % self.pk


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["number", "auth_accepeted", "created_at"]
        widgets = {
            'gender': Select(attrs={'data-native-menu': 'false', 'data-placeholder': 'true', 'placeholder': 'Selectionnez...'}),
            'lastname': TextInput(attrs={'placeholder': 'Nom'}),
            'firstname': TextInput(attrs={'placeholder': 'Prenom'}),
            'address': TextInput(attrs={'placeholder': 'Adresse'}),
            'postcode': TextInput(attrs={'placeholder': 'NPA'}),
            'locality': TextInput(attrs={'placeholder': 'Localite'}),
            'country': TextInput(attrs={'placeholder': 'Pays'}),
            'height': TextInput(attrs={'placeholder': 'Hauteur (en cm)'}),
            'weight': TextInput(attrs={'placeholder': 'Poids (en kg)'}),
            'distinctive_signs': TextInput(attrs={'placeholder': 'Signe(s) distinctif(s)'}),
            'education': TextInput(attrs={'placeholder': 'Formation'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'origin': TextInput(attrs={'placeholder': 'Origine'}),
        }


class Poll(models.Model):
    question = models.TextField()
    template = models.TextField()
    sequence = models.SmallIntegerField()
    next = models.ForeignKey('self', blank=True, null=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question


class Choice(models.Model):
    number = models.CharField(max_length=500, blank=True, null=True)
    choice_text = models.CharField(max_length=200, blank=True, null=True)
    polls = models.ManyToManyField(Poll)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    created_at = models.DateTimeField(auto_now_add=True)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ["user", "poll", "choice", "created_at"]


class Friend(models.Model):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)