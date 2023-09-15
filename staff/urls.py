from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('add_album/<int:pk>', views.add_album, name='add_album')   
]