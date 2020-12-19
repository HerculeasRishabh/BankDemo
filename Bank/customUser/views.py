from django.shortcuts import render, redirect
from .admin import UserCreationForm
from django.contrib import messages


def home( request ):
    return render(request, 'customUser/home.html')

def register( request ):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'customUser/register.html', {'form': form})
