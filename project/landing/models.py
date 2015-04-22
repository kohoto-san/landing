from django.db import models
from django import forms

# Create your models here.


class Emails(models.Model):

    email = models.EmailField()

    def __str__(self):
       return self.email


class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'textbox',}))
