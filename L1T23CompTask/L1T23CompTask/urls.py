"""L1T23CompTask URL Configuration

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
from django.urls import path, include

"""
URL patterns are a list of groups of URLs 
by app, and allow the render request functions
in individual app views.py to be called
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', include("userauth.urls")),
    path('personalbio/', include('personalbio.urls')),
    path('myguitars/', include('myguitars.urls', namespace='myguitars')),
    path('polls/', include('polls.urls')),
    path('shopping/', include('shopping.urls')),
]
