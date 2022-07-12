from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('accounts/signup', views.signup, name='signup'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='cars_delete'),
    path('upgrades/', views.UpgradeList.as_view(), name='upgrades_index'),
    
]