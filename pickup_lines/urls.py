from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/romantic/', views.get_romantic_pickup_line, name='romantic_api'),
    path('api/techy/', views.get_techy_pickup_line, name='techy_api'),
]
