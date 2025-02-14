from django import forms

class RegForm(forms.Form):
    fname = forms.CharField(label='First Name:', widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter your First name'}))
    lname = forms.CharField(label='Last Name:', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your Last name'}))
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'Enter Your Password'}))
    mobile = forms.IntegerField(label='Mobile No:',widget=forms.NumberInput(attrs={
        'class':'form-control','placeholder':'Enter your mobile number'}))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your Email'}))
    dob = forms.CharField(label='Date of birth:', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your date of birth'}))
    gender = forms.CharField(label='Gender:', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your Gender'}))