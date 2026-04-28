from django.urls import path
from . import views

urlpatterns = [
    path('', views.DestinationsList.as_view(), name='home'),
]
