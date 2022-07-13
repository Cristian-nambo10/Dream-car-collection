from django.contrib import admin
from .models import Car, Photo, Upgrade

# Register your models here.
admin.site.register(Car)

admin.site.register(Photo)

admin.site.register(Upgrade)