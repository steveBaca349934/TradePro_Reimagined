from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Username'}))

    password = forms.CharField(label="Password",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Password'}))

class AccountCreationForm(forms.Form):
    email = forms.CharField(label="Email",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Email'}))

    username = forms.CharField(label="Username",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Username'}))

    password = forms.CharField(label="Password",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Password'}))

    first_name = forms.CharField(label="First_Name",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'First_Name'}))

    last_name = forms.CharField(label="Last_Name",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Last_Name'}))
