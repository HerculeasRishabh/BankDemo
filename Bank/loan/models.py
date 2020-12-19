from django.db import models
from customUser.models import MyUser

class UserLoan( models.Model ):

    DURATION_CHOICES = [
        (3, '3 - Months'),
        (6, '6 - Months'),
        (9, '9 - Months'),
        (12, '12 - Months'),
    ]

    INTEREST_RATE_CHOICES = [
        (5, '5% PA'),
        (10, '10% PA'),
    ]
    
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    duration =  models.IntegerField(choices=DURATION_CHOICES, default=3)
    rate_of_interest = models.IntegerField(choices=INTEREST_RATE_CHOICES, default=5)

    def __str__( self ):
        return f'{self.user.username} - {self.amount}'