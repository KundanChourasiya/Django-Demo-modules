from django import forms

class ContactForm(forms.Form):
    fname = forms.CharField(label='First name:', max_length=20, required=True,widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter your name'}))
    lname = forms.CharField(label='last Name:', widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter your last name'}))
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter your Username'}))
    password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Enter your Password'}))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={
        'class':'form-control','placeholder':'Enter your Email Id'}))
    mobile = forms.IntegerField(label='Mobile No:',widget=forms.NumberInput(attrs={
        'class':'form-control','placeholder':'Enter your Mobile Number'}))

