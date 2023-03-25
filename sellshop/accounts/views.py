from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html' )


def my_account(request):
    return render(request, 'accounts/my-account.html' )

