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


class ChangePDub(forms.Form):

    old_password = forms.CharField(label="Old Password",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Old Password'}))

    new_password = forms.CharField(label="New Password",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'New Password'}))


class RecoveryQuestions(forms.Form):

    question_one = forms.CharField(label="Question One, what was your first grade teacher\'s name ? ",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Question One'}))

    question_two = forms.CharField(label="Question Two, what was/is your favorite pet\'s name ? ",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Question Two'}))

class RecoverAccountForm(forms.Form):

    username = forms.CharField(label="Username",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Username'}))

    question_one = forms.CharField(label="Question One, what was your first grade teacher\'s name ? ",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Question One'}))

    question_two = forms.CharField(label="Question Two, what was/is your favorite pet\'s name ? ",required= False,
    widget= forms.TextInput
    (attrs={'placeholder':'Question Two'}))


