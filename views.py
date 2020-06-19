from django.shortcuts import render
from django.http import HttpResponse
from .models import office
from .models import record

# Create your views here.
def index(request): 
	return render(request,"test/index.html")
def home(request):
	print("it working")
	request.method=='POST'
	if office.objects.filter(name=request.POST['name'],password=request.POST['password']).exists():
		return render(request,"test/home.html")
	else:
		print("not work")
		return render(request,"test/index.html")

def details(request):
	return render(request,"test/details.html")
def store(request): 
	print("it working")
	name=request.POST['name']
	fathername=request.POST['fathername']
	gender=request.POST['gender']
	dob=request.POST['dob']
	email=request.POST['email']
	mark=request.POST['mark']
	fees=request.POST['fees']
	phonenumber=request.POST['phonenumber']
	address=request.POST['address']
	records=record(name=name,fathername=fathername,gender=gender,dob=dob,
	 email=email,mark=mark,fees=fees,phonenumber=phonenumber, address=address)
	records.save()
	return render(request,"test/details.html")