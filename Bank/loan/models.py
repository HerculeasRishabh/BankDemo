from django.db import models
from customUser.models import MyUser
from django.utils import timezone

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
    date_applied = models.DateField(default=timezone.now)

    def __str__( self ):
        return f'{self.user.username} - {self.amount}'

    @property
    def compound_interest( self ):
        ''' By defauly we conpound every quater '''
        compounding_period = self.duration/3
        ci_amount = self.amount*( 1 + self.rate_of_interest/(compounding_period*100) )**self.duration
        return ci_amount

    @property
    def due_date( self ):
        ''' End date of loan '''
        from dateutil.relativedelta import relativedelta
        return self.date_applied + relativedelta(months=self.duration)
