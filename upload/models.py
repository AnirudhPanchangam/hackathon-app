from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetails(models.Model):
	# course = models.ManyToManyField()
	user = models.ForeignKey(User,on_delete = models.CASCADE)

class CoursesList(models.Model):
	course = models.CharField(max_length = 140)
