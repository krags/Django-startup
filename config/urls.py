from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from quotes.views import Register


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('my_app.urls')),
    path('blog/', include('blog.urls')),
    path('resume_pics/', include('resume_pics.urls')),

    path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name ='register-success'),
    path('register/', Register.as_view(), name='register'),
]