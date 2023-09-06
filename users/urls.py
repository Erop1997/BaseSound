from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
<<<<<<< HEAD
    path('sign_out/', views.sign_out, name='sign_out'),
    path('reset_password/', views.reset_password, name='reset_password')
=======
    path('sign_out/', views.sign_out, name='sign_out')
>>>>>>> 75cbddd (sign_in_up)
]