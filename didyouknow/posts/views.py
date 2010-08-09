from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is Index Page")

def login(request):
    return HttpResponse("This is Login Page")


