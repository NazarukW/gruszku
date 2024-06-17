from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Uwierzytelnienie zakończyło się sukcesem")
                else:
                    return HttpResponse("Konto jest zablokowane")
            else:
                return HttpResponse("Nieprawidłowe dane logowania")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form': form})

@login_required
def dashboard(request):
    return render(request,
                  "account/dashboard.html",
                  {"section": "dashboard"})

@login_required
def user_logout(request):
    logout(request)
    return render(request,
                  "registration/logged_out.html",
                  {})