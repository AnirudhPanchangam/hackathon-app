from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'upload_index'),
    
    ]
