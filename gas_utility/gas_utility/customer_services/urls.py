from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('submit/', views.submit_request, name='submit_request'),
    path('requests/', views.view_requests, name='view_requests'),
]
