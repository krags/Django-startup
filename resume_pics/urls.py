# resume_pics.urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# Original code below
urlpatterns = [
    path('', views.photo_carousel, name='photo_carousel'),
]

print('settings.MEDIA_URL ', settings.MEDIA_URL)
print('settings.MEDIA_ROOT ', settings.MEDIA_ROOT)

print(" ")
