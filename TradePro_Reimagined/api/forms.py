from django import forms

class EmailForm(forms.Form):
    email = forms.CharField(label="Email",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Email'}))

class PasswordForm(forms.Form):
    password = forms.CharField(label="Password",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Password'}))