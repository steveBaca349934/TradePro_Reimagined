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
    

class RiskAssessmentTest(forms.Form):

    question_one = forms.CharField(label="Question One: I plan to begin withdrawing money from my investments in",required= True,
    widget= forms.Select
    (choices = [(1,"Less than 1 year")
               ,(2,"1 - 5 years")
               ,(3,"6 - 10 years")
               ,(4,"10 - 15 years")
               ,(5,"15+ years")]))

    question_two = forms.CharField(label="Question Two: As I withdraw money, I plan to spend money over  a period of ",required= True,
    widget= forms.Select
    (choices = [(1,"Less than 1 year")
               ,(2,"1 - 5 years")
               ,(3,"6 - 10 years")
               ,(4,"10 - 15 years")
               ,(5,"15+ years")]))

    question_three = forms.CharField(label="Question Three: When making a long-term investment, I plan to keep the money invested for ",required= True,
        widget= forms.Select
        (choices = [(1,"Less than 1 year")
                ,(2,"1 - 5 years")
                ,(3,"6 - 10 years")
                ,(4,"10 - 15 years")
                ,(5,"15+ years")]))

    question_four = forms.CharField(label="Question Four: From September 2008 through November 2008, U.S. stocks lost more than 31% of their value. If I owned a stock investment that lost 30% of its value in a short period,\
    I would … (If you owned stocks in 2008, please select the answer that matches your actions at that time.) ",required= True,
            widget= forms.Select
            (choices = [(1,"Sell all of the remaining investments")
                    ,(2,"Sell some of the remaining investments")
                    ,(3,"Hold on to the investments and do nothing")
                    ,(4,"Buy more of the investment")
                    ,(5,"Bet your whole net worth on a leveraged call option")]))


    question_five = forms.CharField(label="Question Five: Generally, I prefer investments with few dramatic ups or downs in value, \
    and I am willing to accept the lower returns these investments may produce. ",required= True,
            widget= forms.Select
            (choices = [(1,"I strongly disagree")
                    ,(2,"I disagree")
                    ,(3,"I somewhat agree")
                    ,(4,"I agree")
                    ,(5,"I strongly agree")]))
    

    question_six = forms.CharField(label="Question Six: I would invest in a mutual fund based only on a brief\
     conversation with a friend, coworker or relative. ",required= True,
                widget= forms.Select
                (choices = [(1,"I strongly disagree")
                        ,(2,"I disagree")
                        ,(3,"I somewhat agree")
                        ,(4,"I agree")
                        ,(5,"I strongly agree")]))

    question_seven = forms.CharField(label="Question Seven: Others describe you as ambitious and willing to take risks ",required= True,
                    widget= forms.Select
                    (choices = [(1,"I strongly disagree")
                            ,(2,"I disagree")
                            ,(3,"I somewhat agree")
                            ,(4,"I agree")
                            ,(5,"I strongly agree")]))

    question_eight = forms.CharField(label="Question Eight: My current and future income sources (such as salary or pension) are ",required= True,
                    widget= forms.Select
                    (choices = [(1,"Very unstable")
                            ,(2,"Unstable")
                            ,(3,"Somewhat stable")
                            ,(4,"Stable")
                            ,(5,"Very stable")]))

    question_nine = forms.CharField(label="What is the total amount of $ you are willing to invest?",required= True,
        widget= forms.TextInput
        (attrs={'placeholder':'$ Amount'}))

class FinacialIndex(forms.Form):
    OPTIONS = (
        ("S&P", "S&P500"),
        ("DJIA", "DJIA"),
        ("NASDAQ", "NASDAQ"),
    )
    Financials = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)


class MutualFundProviders(forms.Form):
    OPTIONS = (
        ("Vanguard", "Vanguard"),
        ("Fidelity", "Fidelity"),
        ("Schwab", "Schwab"),
        ("T_Rowe", "T_Rowe"),
        ("TD_Ameritrade", "TD_Ameritrade"),
        ("Merrill_Lynch", "Merrill_Lynch"),
    )
    Mutual_Fund = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)