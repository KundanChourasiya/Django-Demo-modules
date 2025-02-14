from django import forms

class ContactForm(forms.Form):
    sname = forms.CharField(max_length=20)
    sloc = forms.CharField(max_length=20)
    semail = forms.EmailField(max_length=50)
