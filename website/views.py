from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    #checkimg if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged in")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging in Please Try Again....")
            return redirect('home')
    else:    
        return render(request, 'home.html', {'records':records})
    
def login_user(request):
       return render(request, 'login.html')
 

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out....")
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate amd login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have sucessfully register")
            return redirect('home')
    else:
        form = signUpForm()
        return render(request, 'register.html', {'form':form})
    
        return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # check if user is logged in
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be Logged in to view this page")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be Logged in to delete this record")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Sucessfully...")
                return redirect('home')          
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be login in to created a Record..")
        return redirect('home')



def update_record(request, pk):
    if request.user.is_authenticated:
        update_it = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=update_it)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated Successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form}) 
    else:
        messages.success(request, 'You Must be Logged In.....')
        return redirect('home')
    
    

    