from django.db import models
from core.models import VideoDetails
import datetime
from django.utils  import timezone
from django.contrib.auth.models import User
# Create your models here.
class Courses(models.Model):
    courses = models.CharField(max_length = 140)

class Comments(models.Model):
    comment = models.CharField(max_length = 140)
    video = models.ForeignKey(VideoDetails,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date_time = models.DateTimeField(default = timezone.now())