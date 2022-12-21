from django.urls import path
from . import views

app_name = 'myguitars'
"""
The following URL patterns call the 
functions defined in views.py. in turn 
these" URL patterns are called by the 
project level urls file in the root 
directory
"""
urlpatterns = [
    path('index', views.index, name='index'),
    path('bacchus', views.bacchus, name='bacchus'),
    path('ebmm', views.ebmm, name='ebmm'),
    path('prs', views.prs, name='prs'),
    path('rk', views.rk, name='rk'),
    path('strat', views.strat, name='strat'),
    path('gower', views.gower, name='gower'),
    path('slo', views.slo, name='slo'),
    path('vids', views.vids, name='vids'), 
]