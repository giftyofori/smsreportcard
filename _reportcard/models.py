from django.db import models
from django.admin.site import admin
from random import randinit

class Student(models.Model):
	first_name = models.CharField(max-length = 50 )
	middle_name = models.CharField(max_length = 50 , blank = True , null = True)
	last_name = models.CharField(max_length = 50)
	def secret_code():
		return "some secret code"
	
	secret_code = models.IntergerField(max_length = 6 , default = secret_code())
	Email = models.EmailField(max_length = 50, blank = True , help_text = "optional" )
	phone_number = models.PhoneNumberField("Phone Number" , max_length = 10)
	city = models.CharField("City or Town" , max_length = 50)
	country = models.CharField("Citizenship" , max_length = 50)
	
	def __unicode__(self):
		return self.first_name
	class Meta: 
		db_table = students


class Student_Info(models.Model):
	student = models.ForeignKey(Student)
	class_id = models.ForeignKey(Class)
	class_teacher_id = models.ForeignKey(Teacher)
	mother_name = models.Charfield(max_length = 50)
	father_name = models.CharFiled(max_length = 50)
	
	def __unicode__(self):
		return self.id

	class Meta:
		db_table = student_info

class Teacher(models.Model):
	subject = models.ForeignKey(Subject)
	id = models.IntegerField(max_length = 6)
	name = models.CharField(max_length = 50)
	

class Subject(models.Model):
	
	name  = models.CharFeild(max_length = 50)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = Subject

class Teaches(models.Model):
	teacher_id = models.IntegerField(max_length= 8)
	subject_name = models.CharField(max_length = 50)
	class_name = models.CharField(max_length = 50)
	period = None
	
	
	def __unicode__(self):
		return self.id


	class Meta:
		db_table = teaches





	 
