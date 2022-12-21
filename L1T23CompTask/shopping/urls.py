from django.urls import path
from . import views

app_name = 'shopping'
"""
The following URL pattern calls the 
functions defined in views.py. in turn 
these" URL patterns are called by the 
project level URL file in the root 
directory
"""
urlpatterns = [
    path('main', views.main, name="main"),
]