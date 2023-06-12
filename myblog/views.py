from django.shortcuts import render, redirect
from .models import blogs_db
from . import urls
from .models import accounts
from django.http import HttpResponseRedirect

# Create your views here.
def blogHome(request):
    blogs_data=blogs_db.objects.all()
    data={
        'blogs_data':blogs_data
    }
    return render(request,"index.html",data)

def getStarted(request):
    myacc_user = accounts.objects.all()
    data_acc = {
        'myacc_user': myacc_user
    }
    data = {}

    if request.method == "POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")

        if Username == "" and Password == "":
            return render(request, "login.html", {'error1': True, 'error2': True})
        elif Username == "" and Password != "":
            data = {
                'Password': Password,
            }
            return render(request, "login.html", {'error1': True, **data})
        elif Username != "" and Password == "":
            data = {
                'Username': Username,
            }
            return render(request, "login.html", {'error2': True, **data})
        else:
            # Check if username and password match in the database
            matching_accounts = accounts.objects.filter(Username=Username, Password=Password)
            if matching_accounts.exists():
                # Redirect to success page
                return redirect('success')
            else:
                # Render login page with an error message
                return render(request, "login.html", {'error3': True})

    return render(request, "login.html", data_acc, **data)

def aboutUs(request):
    
    return render(request, "about.html")

def blogs(request):
    return render(request, "blogs.html")

def contactUs(request):
    return render(request, "contact.html")


def signUp(request):
    data = {}
    if request.method == "POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        Email = request.POST.get("Email")

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


def newacc(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get("Password")
        Email = request.POST.get("Email")

        if not Username or not Password or not Email:
            return signUp(request)  # Call signUp function and pass the request object

        en = accounts(Username=Username, Password=Password, Email=Email)
        en.save()

        return HttpResponseRedirect('success')


def success_view(request):
    return render(request, 'success.html')
