from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add URL pattern for the root URL
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
