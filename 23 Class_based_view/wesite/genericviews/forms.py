from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Your name'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter your description'}))