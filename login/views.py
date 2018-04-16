from django.shortcuts import render,redirect
from login.forms import LoginForm
from django.utils import timezone
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
# from core.models import StudentDetails,TeacherDetails
# Create your views here.
def index(request):
	if request.method == 'POST':
		
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['email']
			# password = form.cleaned_data['password']
			print(username)
			user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
			try:
				
				login(request,user)
				return redirect('/')

			except:
				return render(request,'login/index.html',{"error_message":"Username or password incorrect"})			
	form = LoginForm()
	return render(request,"login/index.html",{"form":form})

def logoutView(request):
	logout(request)
	return redirect('/')