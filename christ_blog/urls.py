from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.versicle_list, name='versicle_list'),
    path('<int:pk/', views.versicle_teaching, name='versicle_teaching'),
]