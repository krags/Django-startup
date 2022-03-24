from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_app, name='my_app'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('mypost/', views.mypost, name='mypost'),
]