from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
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
	if request.method=='POST' and request.FILES['image']:
		files=request.FILES['image']
		fs=FileSystemStorage()
		image=fs.save(files.name,files)
		print(image)
		print(type(image))
	else:
		print("filed")
	name=request.POST['name']
	fathername=request.POST['fathername']
	gender=request.POST['gender']
	dob=request.POST['dob']
	email=request.POST['email']
	mark=request.POST['mark']
	fees=request.POST['fees']
	phonenumber=request.POST['phonenumber']
	address=request.POST['address']
	records=record(image=image, name=name,fathername=fathername,gender=gender,dob=dob,
	 email=email,mark=mark,fees=fees,phonenumber=phonenumber, address=address)
	records.save()
	return render(request,"test/details.html")
def view(request):
	getdetail=record.objects.all()
	return render(request,"test/view.html",{'getdetails':getdetail})
def delete(request,pk):
	print("ok go heard")
	dels=record.objects.get(pk=pk)
	dels.delete()
	return redirect("view")
def edit(request,pk):
	print("fine")
	student=record.objects.get(pk=pk)
	return render(request,"test/edit.html",{'student':student})
def update(request,pk):
	print("process")
	student=record.objects.get(pk=pk)
	student.save()
	return render(request,"test/edit.html",{'student':student})
