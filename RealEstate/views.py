from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime

# def signup(request):
# 	if request.method == "POST":
# 		nm = request.POST['nm']
# 		uname = request.POST['un']
# 		pwd = request.POST['pwd']
# 		role = request.POST['role']
# 		date = datetime.now()
# 		su = 0
# 		staff = 0
    
# 		if role == "admin":
# 			su = 1
# 		elif role == "user":
# 			staff = 1

# 		u = User(first_name=nm, username=uname, password=make_password(pwd), is_superuser=su, is_staff=staff,date_joined=date)
# 		u.save()
# 		messages.success(request,"Registration Successfully Done")
# 		return redirect('/signup/')
# 	return render(request, "signup.html")

#  user registration 
def signup(request):
	if request.method == "POST":
		nm = request.POST['nm']
		lnm = request.POST['lnm']
		email = request.POST['email']
		uname = request.POST['un']
		pwd = request.POST['pwd']
		date = datetime.now()
		

		u = User(first_name=nm, last_name=lnm, email=email, username=uname, password=make_password(pwd), is_staff=True,date_joined=date)
		u.save()
		messages.success(request,"Registration Successfully Done")
		return redirect('/signup/')
	return render(request, "signup.html")
def login_call(request):
	if request.method == "POST":
		uname = request.POST['un']
		pwd = request.POST['pwd']

		user = authenticate(username=uname, password=pwd)
		print(user.date_joined)

		if user:
			login(request, user)
			if user.is_superuser:
				return redirect('/saddmin/dashboard/')
			elif user.is_staff:
				return redirect('/user/index/')
			
		else:

			return redirect('/login/')
		
	return render(request, "login.html")

def logout_call(request):
	logout(request)
	return redirect('/login/')

