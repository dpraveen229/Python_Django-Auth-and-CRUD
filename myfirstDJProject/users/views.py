from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Employee

def home(request):
    return render(request, 'users/home.html')  # Display a home page


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #return redirect('/')  # Redirect to a home page after login
                return render(request, 'users/employee_form.html', {'form': form})
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def employee_form(request):
    if request.method == 'POST':
        if 'submit' in request.POST:  # Check if Submit button is clicked
            name = request.POST.get('name')
            age = request.POST.get('age')
            salary = request.POST.get('salary')
            print(f"Received data: Name={name}, Age={age}, Salary={salary}")
            # Save the employee details in the database
            Employee.objects.create(name=name, age=age, salary=salary)
            return HttpResponse('Employee details have been successfully saved!')

        elif 'exit' in request.POST:  # Check if Exit button is clicked
            return HttpResponse('Thank you!')

    return render(request, 'users/employee_form.html')