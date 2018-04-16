from django.shortcuts import render,redirect
from core.models import StudentDetails,TeacherDetails,VideoDetails
from .forms import RegistrationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
	if request.method == 'POST':
		regForm = RegistrationForm(request.POST)
		if regForm.is_valid():
			username = regForm.cleaned_data["email"]
			try:
				user = User.objects.create_user(username = username,password = regForm.cleaned_data['pwd1'])
				user.email = regForm.cleaned_data['email']
				user.first_name = regForm.cleaned_data['fname']
				user.last_name = regForm.cleaned_data['lname']
				
				user.save()
				user_group = regForm.cleaned_data['user_group']
				user = authenticate(username=regForm.cleaned_data['email'], password=regForm.cleaned_data['pwd1'])
				login(request,user)
				group = Group.objects.get(name=user_group)
				
				user.groups.add(group)
				if user_group == 'teacher':
					teach = TeacherDetails()
					print(group)
					teach.teacher_user = user
					teach.phone = regForm.cleaned_data['phone']
					print(teach.teacher_user)
					teach.save()
					return redirect('/login/')
				elif user_group == 'student':
					vd = VideoDetails.objects.filter(pk = 1)
					stud = StudentDetails()
					stud.student_user = user
					# stud.teachers.add(request.user)
					stud.current_video = vd[0]
					stud.phone = regForm.cleaned_data['phone']
					stud.save()
				return redirect('/login/')
			except:
				form = RegistrationForm()
				return render(request,"register/index.html",{"error":"Email already exists","form":form})
		else:
			return redirect('/')
	form = RegistrationForm()
	return render(request,"register/index.html",{"form":form})