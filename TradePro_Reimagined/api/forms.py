from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label="Email",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Email'}))

    password = forms.CharField(label="Password",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Password'}))
