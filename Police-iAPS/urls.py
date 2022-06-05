"""prison URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from IAPS_app.views import IndexView,Jailer_Reg,Medical_Reg,Forgot_Password
from IAPS_app import admin_urls,warden_urls,h_officer_urls
from django.conf.urls.static import static
from . import settings



urlpatterns = [
    path('admin/',admin_urls.urls()),
    path('warden/',warden_urls.urls()),
    path('health_officer/',h_officer_urls.urls()),
    path('', IndexView.as_view()),
    path('jailer_reg',Jailer_Reg.as_view()),
    path('medical_reg',Medical_Reg.as_view()),
    path('forgot_password',Forgot_Password.as_view()),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
