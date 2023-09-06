from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
<<<<<<< HEAD
    path('song/', views.song , name='song'),
]
=======
    path('song<int:pk>/', views.song , name='song'),
]
>>>>>>> 634be568656fb55ffb14a9a1b1c5e141c338dbed
