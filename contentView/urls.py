from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'view_index'),
    path('<str:course_name>/',views.video,name = 'view_video'),
    path('view/<int:obj_id>/',views.display,name = 'disp_video'),
    
    ]
