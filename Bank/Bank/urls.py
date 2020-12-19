"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from customUser import views as customUser_views
from loan import views as loan_views

urlpatterns = [
    path( '', customUser_views.home, name='home'),
    path( 'register/', customUser_views.register, name='register'),

    path( 'loan/', loan_views.loan, name='loan'),

    path( 'user/', include('customUser.urls')),

    path( 'admin/', admin.site.urls),
]
