"""dcaf_drive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "DCAF Drive";
admin.site.site_header = "DCAF Drive";
admin.site.index_title = "Dashboard";

urlpatterns = [
    path('', admin.site.urls),
    #url(r'^main/', include('django_sb_admin.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^', include('filer.server.urls')),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name = 'django_sb_admin/examples/login.html'), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)