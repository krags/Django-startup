from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    # path('contact', views.contact, name='contact'),
    # path('home_view', views.home_view, name='home_view'),
    # path('<str:pagename>', views.index, name='index'),
]


