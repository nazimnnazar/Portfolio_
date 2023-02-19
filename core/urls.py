from django.urls import path
from .views import *
urlpatterns = [
    path('',views.home,name='home')
]
