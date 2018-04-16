from django.shortcuts import render
from core.models import VideoDetails,StudentDetails,TeacherDetails
from .models import Comments
# Create your views here.

def index(request):
	selection = []
	vd = VideoDetails.objects.all()
	for i in range(0,len(vd)):
		if vd[i].course in selection:
			pass
		else:
			selection.append(vd[i].course)

	return render(request,'contentView/selection.html',{"selection":selection})


def some(request):
	vd = VideoDetails.objects.filter()
	for obj in vd:
		print(obj.course)
	
	# print(vd.document)
	return render(request,"contentView/index.html",{"vd":vd})


def video(request,course_name):
	vd = VideoDetails.objects.filter(course = course_name)
	# comment = Comments.objects.filter(video  = vd[0])
	return render(request,"contentView/video.html",{"vd":vd})

def display(request,obj_id):
	vd = VideoDetails.objects.filter(id = obj_id)
	# comments = Comments.objects.filter(video = vd)
	# print(comments)
	print(vd)
	return render(request,'contentView/display.html',{"vd":vd})