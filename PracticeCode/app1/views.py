from django.shortcuts import render
from django.http import HttpResponse
from .models import UsersInfo
from .forms import UserForm

# Create your views here.


# def index(request):
#     return HttpResponse("<h1> This is index page <h1>")

def index(request):
    return render(request, 'app1/index.html')


def user_info(request):
    users_list = UsersInfo.objects.order_by('first_name')
    user_dict = {'access_user': users_list}
    return render(request, 'app1/userslist.html', context=user_dict)


def user_form(request):
    user_form = UserForm()

    # This run when we hit submit button
    if request.method == "POST":
        user_form = UserForm(request.POST)

    if user_form.is_valid():
        # This line alone save data to database
        # user_form.save(commit=True)
        # To save data to database
        obj = UsersInfo()
        print("Form validation is successful")
        obj.first_name = user_form.cleaned_data['first_name']
        print("First Name : ", user_form.cleaned_data['first_name'])
        obj.last_name = user_form.cleaned_data['last_name']
        print("Last Name : ", user_form.cleaned_data['last_name'])
        obj.email = user_form.cleaned_data['email']
        print("Email : ", user_form.cleaned_data['email'])
        obj.save()
        print("Data is saved in database")
        # This will simply return us to home page
        return index(request)

    return render(request, 'app1/userform.html', {'form': user_form})


