from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info, name='get_info'),
]
