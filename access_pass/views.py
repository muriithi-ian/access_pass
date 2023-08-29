from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def access_form(request):
    return render(request, 'access_forms.html')

def success(request):
    return render(request, 'success.html')