from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import Record

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Username or Pw, try again :)')
            return redirect('home')
    else:
        return render(request, 'home.html', {
            'records': records
        })

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user registered')
            return redirect('home')
        else:
            return render(request, 'register.html', {
                'form': form
            })
    else:
        form = SignUpForm()
        return render(request, 'register.html', {
            'form': form
        })

def customer_view(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        return render(request, 'customer.html', {
            'customer': customer
        })
    else:
        messages.success(request, 'You must be logged in to see this page!')
        return redirect('home')

def delete(request, pk):
    if request.user.is_authenticated:
        del_object = Record.objects.get(id=pk)
        del_object.delete()
        messages.success(request, 'Instance deleted!')
        return redirect('home')
    else:
        messages.success(request, 'You have to be logged in order to be able to delete instance!')
        return redirect('home')

def add_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddCustomerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'The Customer has been added!')
                return redirect('home')
            else:
                messages.success(request, 'The form is not valid')
                return redirect('add_customer')
        else:
            form = AddCustomerForm()
            return render(request, 'add_customer.html', {
                    'form': form
                })
    else:
        messages.success(request,'You need to be logged in in order to add new customers!')
        return redirect('home')

def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Record.objects.get(id=pk)
        if request.method == 'POST':
            form = AddCustomerForm(request.POST, instance=current_customer)
            if form.is_valid():
                form.save()
                messages.success(request, 'Customer updated successfully')
                return redirect('home')
        else:
            form = AddCustomerForm(instance=current_customer)
            return render(request, 'update_customer.html', {
                'form': form
            })
    else:
        messages.error(request, 'You need to be logged in to update changes!')
        return redirect('home')