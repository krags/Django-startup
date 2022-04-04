# config.urls (main)
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from quotes.views import Register

# These are needed for image url to work.
from django.conf import settings
from django.conf.urls.static import static


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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
