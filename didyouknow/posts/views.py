from django.http import HttpResponse
# Create your views here.

#index page
def index(request):
    return HttpResponse("This is Index Page")

#login page
def login(request):
    return HttpResponse("This is Login Page")

#about page
def about(request):
    return HttpResponse("This is about page")

#term and policy page:
def term_and_policy(request):
    return HttpResponse("This is Term and Policy Page")


