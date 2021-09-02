from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # linking profile to the user
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic =request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))

@login_required
def special(request):
    return HttpResponse('You are successfully logged in!')


def user_login(request):

    if request.method == 'POST':
        # Getting value directly from html page
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Checking if the user is valid
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("Some one else tried to login!")
            print("UserName : {}, Password : {}".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'basic_app/login.html', {})


