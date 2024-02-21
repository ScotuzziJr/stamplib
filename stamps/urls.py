from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection, name='collection'),
    path('new_stamp/', views.new_stamp, name='new_stamp'),
    path('stamp/<str:pk>/', views.stamp, name='stamp'),
    path('delete_stamp/<str:pk>/<str:category>/', views.delete_stamp, name='delete_stamp'),
]
