from django.urls import path
from . import views
urlpatterns = [
    path('protfolio/',views.protfolio,name='protfolio'),
]