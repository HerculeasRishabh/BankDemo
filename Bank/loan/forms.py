from django import forms
from .models import UserLoan
from customUser.models import MyUser

class LoanForm( forms.ModelForm ):

    class Meta:
        model = UserLoan

        fields = ['amount', 'duration', 'rate_of_interest']