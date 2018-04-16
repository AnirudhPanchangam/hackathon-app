from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'core_index'),
    path('search/',views.search,name = 'search'),
    
    ]
