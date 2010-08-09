from django.http import HttpResponse
# Create your views here.

#index page
def index(request):
    return HttpResponse("This is Index Page")

#signup page
def signup(request):
    return HttpResponse("This is signup Page")

#login page
def login(request):
    return HttpResponse("This is Login Page")

#about page
def about(request):
    return HttpResponse("This is about page")

#term and service page:
def term_and_service(request):
    return HttpResponse("This is Term and Service Page")

#policy page
def policy(request):
    return HttpResponse("This is policy page")

#help page
def help(request):
    return HttpResponse("This is Help Page")

#show user profile page
def show_user(request, fullname):
    return HttpResponse("You're viewing %s Profile " % fullname )