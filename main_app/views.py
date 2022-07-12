from distutils.log import error
from django.shortcuts import redirect, render
from .models import Car, Photo
from django.contrib.auth import login
import boto3, uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'catcollector-avatar-cn'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', { 'car': car})

def add_photo(request, car_id):
    photo_file = request.Files.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except Exception as error:
            print('Error uploading photo: ', error)
            return redirect('detail', car_id=car_id)

    return redirect('detail', car_id=car_id)


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
