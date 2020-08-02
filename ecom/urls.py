
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    
    path('', include('home.urls')),
    path('registration', include('members.urls')),
    re_path('admin/', include(wagtailadmin_urls)),
    re_path('documents/', include(wagtaildocs_urls)),
    re_path('pages/', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
