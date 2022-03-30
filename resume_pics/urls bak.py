from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

#3-29-22
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Original code below
urlpatterns = [
    path('', views.photo_carousel, name='photo_carousel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
