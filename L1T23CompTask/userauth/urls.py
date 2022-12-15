from django.urls import path
from . import views

app_name = 'userauth'
urlpatterns = [
    
    path('', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('authenticate_user/', views.authenticate_user,name='authenticate_user'),
]