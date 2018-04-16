from django.contrib import admin
from .models import VideoDetails,StudentDetails,TeacherDetails
# Register your models here.


admin.site.register(VideoDetails)
admin.site.register(StudentDetails)
admin.site.register(TeacherDetails)