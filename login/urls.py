from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'login_index'),
    path('logout/',views.logoutView,name = 'logout'),
    ]
