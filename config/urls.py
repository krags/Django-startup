from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from quotes.views import Register
from django.conf.urls.static import static
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', blog_views.home, name='home'),
    path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name ='register-success'),
    path('register/', Register.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

