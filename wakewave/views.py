from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        return HttpResponse("user has been screated sucessfully")
    return render(request, 'signup.html')


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

