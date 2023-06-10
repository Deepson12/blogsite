from django.shortcuts import render, redirect
from .models import User
from . import urls

# Create your views here.
def blogHome(request):
    
    return render(request,"index.html")


def getStarted(request):
    return render(request, "login.html")

def aboutUs(request):
    
    return render(request, "about.html")

def blogs(request):
    return render(request, "blogs.html")

def contactUs(request):
    return render(request, "contact.html")

def signUp(request):
    data={}
    if request.method == "POST":
        

        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        Email=request.POST.get("Email")
    
        if Username == "" and Password == "" and Email == "":
            return render(request, "signup.html", {'error1': True, 'error2': True, 'error3': True})
        elif Username == "" and Password == "" and Email != "":
            data = {
                'Email': Email
            }
            return render(request, "signup.html", {'error1': True, 'error2': True, **data})
        elif Username == "" and Password != "" and Email!= "":
            data = {
                'Email': Email,
                'Password': Password,
            }
            return render(request, "signup.html", {'error1': True, **data})
        elif Username != "" and Password == "" and Email == "":
            data = {
                'Username': Username
            }
            return render(request, "signup.html", {'error2': True, 'error3': True, **data})
        elif Username != "" and Password != "" and Email== "":
            data = {
                'Username': Username,
                'Password': Password,
            }
            return render(request, "signup.html", {'error3': True, **data})
        
        elif Username != "" and Password == "" and Email!= "":
            data = {
                'Username': Username,
                'Email': Email,
            }
            return render(request, "signup.html", {'error2': True, **data})
        elif Username =="" and Password != "" and Email =="":
            data = {
                'Password':Password
            }
            return render(request, "signup.html", {'error1': True, 'error3': True, **data})
        


    return render(request, "signup.html", data)
    