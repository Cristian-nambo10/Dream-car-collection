from distutils.log import error
from django.shortcuts import redirect, render
from .models import Car
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', { 'car': car})

def signup(request):
    error_messages = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_messages = 'Invalid Info - Try Again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_messages': error_messages
    })
