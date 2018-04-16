from django.db import models
from django.contrib.auth.models import User
# Create your models here.
course = ""
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.teacher.username,instance.course,filename)
class VideoDetails(models.Model):
    video_name = models.CharField(max_length = 140)
    teacher = models.ForeignKey(User,on_delete = models.CASCADE,related_name="teacher_who_uploaded")
    course = models.CharField(max_length = 140)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to=user_directory_path)



class StudentDetails(models.Model):
    course  = models.CharField(max_length = 140,default = "none")
    teachers = models.ManyToManyField(User,related_name="student_user")
    student_user = models.ForeignKey(User,on_delete = models.CASCADE,related_name="student_details_user")
    score = models.IntegerField(default=0)
    rankings = models.IntegerField(default=200000)
    phone = models.IntegerField(default = 0)
    current_video = models.ForeignKey(VideoDetails,on_delete = models.CASCADE,default = None)

class TeacherDetails(models.Model):
    subject = models.CharField(max_length = 140,default = "none")
    students =  models.ManyToManyField(User,related_name="students_of_teacher")
    teacher_user = models.ForeignKey(User,on_delete = models.CASCADE,related_name="teacher_details_user")
    ratings = models.IntegerField(default = 0)
    phone = models.IntegerField(default = 0)
    rankings = models.IntegerField(default = 200000)


