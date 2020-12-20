from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoanForm
from django.contrib import messages
from .models import UserLoan

@login_required
def loan( request ):
    loans = request.user.userloan_set.all()
    if request.method == "POST":
        loan_form = LoanForm(request.POST)
        if loan_form.is_valid():
            new_loan = request.user.userloan_set.create(
                                                    amount=loan_form.cleaned_data['amount'],
                                                    duration=loan_form.cleaned_data['duration'],
                                                    rate_of_interest=loan_form.cleaned_data['rate_of_interest'], 
                                                    )
            new_loan.save()
            messages.success(request, f'Loan request successful!')
            return redirect('loan')
    else:
        loan_form = LoanForm()
    
    context = {
        'form': loan_form,
        'loans' : loans,
    }
    return render(request, "loan/loan_application.html", context)