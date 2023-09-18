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
    path('home/', views.home , name='home'),
<<<<<<< HEAD
    path('song/', views.song , name='song'),
]
=======
    path('song<int:pk>/', views.song , name='song'),
]
>>>>>>> 634be568656fb55ffb14a9a1b1c5e141c338dbed
>>>>>>> b86369d7d518cab58d85c462a8cf8ccdd3e30ec5
