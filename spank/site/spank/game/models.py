# coding=utf-8
from django.db import models
from django import forms
from django.forms import TextInput, Select

from booth.models import Prize

class Visit(models.Model):
    session_number = models.CharField(max_length=500, blank=True, null=True)
    auth_accepted = models.CharField(max_length=500, blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)
    last_update_at = models.DateTimeField(blank=True, null=True)
    prize = models.ForeignKey(Prize, blank=True, null=True)
    coupable = models.CharField(max_length=50, blank=True, null=True)
    contact_access = models.CharField(max_length=10, blank=True, null=True)
    notified = models.BooleanField(default=False)
    anonymized = models.BooleanField(default=False)
    registered = models.BooleanField(default=False)
    cluster = models.PositiveSmallIntegerField(default=0)
    winner = models.BooleanField(default=False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.number

    def get_absolute_url(self):
        return "/game/qrcode/%i/" % self.pk


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["number", "auth_accepted", "created_at", "updated_at", "last_update_at", "prize", "coupable",
                   "contact_access", "notified", "anonymized", "registered", "cluster", "winner"]
        widgets = {
            'gender': Select(attrs={'data-native-menu': 'false', 'data-placeholder': 'true', 'placeholder': 'Selectionnez...'}),
            'lastname': TextInput(attrs={'placeholder': 'Nom'}),
            'firstname': TextInput(attrs={'placeholder': 'Prenom'}),
            'address': TextInput(attrs={'placeholder': 'Adresse'}),
            'postcode': TextInput(attrs={'placeholder': 'NPA'}),
            'locality': TextInput(attrs={'placeholder': 'Localite'}),
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
    updated_at = models.DateTimeField(auto_now=True)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ["user", "poll", "choice", "created_at"]


class Friend(models.Model):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.email