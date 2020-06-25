from django.db import models

# Create your models here.
class office(models.Model):
	name=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	def __str__(self):
    		return self.name
gender_choices=[
	('male','Male'),
	('female','Female')
]
class record(models.Model):
	image = models.ImageField(upload_to = 'image/') 
	name=models.CharField(max_length=200)
	fathername=models.CharField(max_length=200)
	gender=models.CharField(choices=gender_choices, max_length=200)
	dob=models.DateField()
	email=models.CharField(max_length=200)
	mark=models.IntegerField()
	fees=models.IntegerField()
	paid=models.IntegerField()
	phonenumber=models.IntegerField()
	address=models.TextField(max_length=200)
	def __str__(self):
    		return self.name

