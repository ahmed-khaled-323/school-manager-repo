from django.urls import path,include
from . import views

urlpatterns = [
    path('' , views.loginsystem,name='login'),
    path('logout', views.logoutsystem,name ='logout')
]