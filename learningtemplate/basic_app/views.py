from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {"name": "Hello world", "number": 100, "email": "hrithik@gmail.com"}
    return render(request, 'basic_app/index.html', context=context_dict)

def others(request):
    return  render(request, 'basic_app/others.html')
