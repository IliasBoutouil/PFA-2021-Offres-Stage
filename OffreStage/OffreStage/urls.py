from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('publications/',include('Publication.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
