from django import forms

class SingupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    salary = forms.IntegerField(label='Salary')