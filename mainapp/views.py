from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, 'index.html')

def userSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #VALIDATE PASSWORD, CHECK IF THE 2 PASSWORDS MATCH
        if password1 != password2:
            return HttpResponse("Passwords do not match")
        #CHECK IF THE USERNAME IS ALREADY TAKEN
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken")
        #CHECK IF EMAIL IS ALREADY REGISTERED
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already registered")
        
        #CREATE A NEW USER
        user = User.objects.create_user(
            username = username,
            first_name = firstName,
            last_name = lastName,
            email = email,
            password = password1
        )
        user.save()
        return HttpResponse('User has been created Successfully')


        #print(username, firstName, lastName, email, password1, password2)
    return render(request, 'signup.html')

def userLogin(request):
    return render(request, 'login.html')