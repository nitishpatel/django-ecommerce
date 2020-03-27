from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm



# Create your views here.
def home_page(request):
    return render(request,"main/index.html",{})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"New Account Created :{username}")
            login(request,user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")


    form = NewUserForm
    
    return render(request,'main/register.html',{"form":form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged Out Successfully")
    return redirect("main:homepage")

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"Logged in as:{username}")
                return redirect("main:homepage")
            else:
                messages.error(request,"User Not Found!")
        
    form = AuthenticationForm()
    return render(request,"main/login.html",{"form":form})