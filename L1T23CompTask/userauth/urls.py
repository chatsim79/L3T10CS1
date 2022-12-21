from django.urls import path
from . import views

app_name = 'userauth'
"""
The following URL pattern calls the 
functions defined in views.py. in turn 
these" URL patterns are called by the 
project level URL file in the root 
directory
"""
urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('authenticate_user/', views.authenticate_user,name='authenticate_user'),
]