<<<<<<< HEAD
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('song<int:pk>/', views.song , name='song'),
    path('upload/<int:pk>', views.upload , name='upload'),
    path('choosing_album/', views.choosing_album , name='choosing_album'),
    path('added/<int:pk>', views.added, name='added')
]
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home , name='home')
]
>>>>>>> d0d848b (some)
