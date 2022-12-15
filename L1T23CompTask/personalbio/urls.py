from django.urls import path
from . import views

app_name = 'personalbio'
"""
The following URL pattern calls the 
functions defined in views.py. in turn 
these" URL patterns are called by the 
project level urls file in the root 
directory

:param module views.home: home function in views.py:
:param string 'home': name assigned to URL

:rtype: rendered webpage
"""
urlpatterns = [
    path('home', views.home, name='home'),
]