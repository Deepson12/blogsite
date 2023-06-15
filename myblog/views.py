from django.shortcuts import render, redirect
from .models import blogs_db
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def getStarted(request):
    if request.user.is_authenticated:
        return redirect('home')
    data = {}

    if request.method == "POST":
        Username = request.POST.get("Username").strip()
        Password = request.POST.get("Password")

        if Username == "" and Password == "":
            return render(request, "login.html", {'error1': True, 'error2': True})
        elif Username == "" and Password != "":
            data = {'Password': Password}
            return render(request, "login.html", {'error1': True, **data})
        elif Username != "" and Password == "":
            data = {'Username': Username}
            return render(request, "login.html", {'error2': True, **data})
        else:
            
            return login_view(request)

    return render(request, "login.html", **data)

def login_view(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get("Password")


        
        user=authenticate(request, username=Username,password=Password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {'error3': True})

def aboutUs(request):
    return render(request, "about.html")


def blogs(request):
    return render(request, "blogs.html")


def contactUs(request):
    return render(request, "contact.html")


def signUp(request):
    data = {}
    if request.method == "POST":
        Username = request.POST.get("Username").strip()
        Password = request.POST.get("Password")
        Email = request.POST.get("Email").strip()

        if Username == "" and Password == "" and Email == "":
            return render(request, "signup.html", {'error1': True, 'error2': True, 'error3': True})
        elif Username == "" and Password == "" and Email != "":
            data = {'Email': Email}
            return render(request, "signup.html", {'error1': True, 'error2': True, **data})
        elif Username == "" and Password != "" and Email != "":
            data = {'Email': Email, 'Password': Password}
            return render(request, "signup.html", {'error1': True, **data})
        elif Username != "" and Password == "" and Email == "":
            data = {'Username': Username}
            return render(request, "signup.html", {'error2': True, 'error3': True, **data})
        elif Username != "" and Password != "" and Email == "":
            data = {'Username': Username, 'Password': Password}
            return render(request, "signup.html", {'error3': True, **data})
        elif Username != "" and Password == "" and Email != "":
            data = {'Username': Username, 'Email': Email}
            return render(request, "signup.html", {'error2': True, **data})
        elif Username == "" and Password != "" and Email == "":
            data = {'Password': Password}
            return render(request, "signup.html", {'error1': True, 'error3': True, **data})

    return render(request, "signup.html", data)


def newacc(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get("Password")
        Email = request.POST.get("Email")

        if not Username or not Password or not Email:
            return signUp(request)

        en = User.objects.create_user(Username, Email, Password)
        en.save()
        return redirect('success')


def success_view(request):
    return render(request, 'success.html')

@login_required(login_url='login')
def default(request):

    blogs_data = blogs_db.objects.all()
    data = {'blogs_data': blogs_data}

    return render(request, "index.html", data)


def logout_page(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    data={
        'username' : request.user.username,
        'email' : request.user.email,
    }
    
    return render(request, "dashboard.html", data)