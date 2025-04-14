from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'index.html')

def userSignup(request):
    return render(request, 'signup.html')

def userLogin(request):
    return render(request, 'login.html')