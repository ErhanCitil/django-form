from django import forms

class ContactForm(forms.Form):
    naam = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    onderwerp = forms.CharField(max_length=255)
    bericht = forms.CharField(max_length=255)

