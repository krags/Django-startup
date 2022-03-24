from django.urls import path
from .views import index
from .views import contact
from .views import home_view


urlpatterns = [
    path('', index),
    #path('', index, {'pagename': ''}, name='home'),
    path('contact', contact, name='contact'),
    path('home_view', home_view, name='home_view'),
    #path('<str:pagename>', index, name='index'),
]