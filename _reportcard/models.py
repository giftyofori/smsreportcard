from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
from tweak import subjectstuple

class Student(models.Model):
	first_name = models.CharField(max_length = 50 )
	middle_name = models.CharField(max_length = 50 , blank = True , null = True)
	last_name = models.CharField(max_length = 50)
	def secret_code():
		return "some secret code"
	
	secret_code = models.IntegerField(max_length = 6 , default = secret_code())
	Email = models.EmailField(max_length = 50, blank = True , help_text = "optional" )
	phone_number = PhoneNumberField("Phone Number" , max_length = 10)
	city = models.CharField("City or Town" , max_length = 50)
	country = models.CharField("Citizenship" , max_length = 50)
	
	def __unicode__(self):
		return self.first_name
	class Meta: 
		db_table = 'students'
class Teaches(models.Model):
	teacher_id = models.IntegerField(max_length= 8)
	subject_name = models.CharField(max_length = 50)

	class_name = models.CharField(max_length = 50)
	period = None
	
	
	def __unicode__(self):
		return self.id


	class Meta:
		db_table = 'teaches'

class Teacher(models.Model):
	#subject = models.ForeignKey(Subject)
	id_number = models.IntegerField(max_length = 6)
	name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.name
	class Meta:
		tb_table = "teacher"


class Student_Info(models.Model):
	student = models.ForeignKey(Student)
	#class_id = models.ForeignKey(Class)
	class_teacher_id = models.ForeignKey(Teacher)
	course = models.CharField(max_length = 50)
	mother_name = models.CharField(max_length = 50)
	father_name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.id

	class Meta:
		db_table = 'student_info'
		verbose_name = "Student Infomation"
		verbose_name_plural = "Student Infomations"


class Subject(models.Model):
	
	name  = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'subject'


class Core_subjects(models.Model):
	subject_name = models.CharField(max_length = 40)

	def __unicode__ (self):
		return self.subject_name

	class Meta:
		db_table = "core subjects"
		verbose_name = "Core Subject"
		permissions = (("Add", "Add Core Subject"),)
'''
# auto save core subjects
core_subjects = ['English', 'Integrated Science', 'Core Mathematics' , 'Social Studies' ]
for i in core_subjects:
	Core_subjects(subject_name = i).save()
'''
class Course(models.Model):
	course_name = models.CharField(max_length = 50)
	number_student = models.IntegerField("Students Offering Course" ,max_length = 4)
	
	def __unicode__(self):
		return self.course_name	

	class Meta:
		db_table = "course"

class Elective_subjects(models.Model):
	subject_name= models.CharField(max_length = 50)
	course  = models.ForeignKey(Course)

	def __unicode__(self):
		return self.subject_name

	class Meta:
		db_table = "elective subjects"
		verbose_name = "Elective Subject"
		verbose_name_plural = "Elective Subjects"

class Report(models.Model):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	date_created = models.DateTimeField(auto_now = True)
	student_name = models.CharField(max_length = 100)
	course = models.CharField(max_length = 50)
	form = models.IntegerField(max_length = 2, choices = FORMS)
	teacher = models.CharField(max_length = 50, default = "logged in user" )
	remark = models.TextField(max_length = 300)

	def __unicode__(self):
		return self.student_name
	
	def get_absolute_url(self):
		return '/report/detail/%s/' % self.id

	class Meta:
		db_table = "report"
	

class Report_content(models.Model):
	report = models.ForeignKey(Report , null = True)
	subject = models.CharField(max_length = 50 , choices = subjectstuple(), default = "English")
	exam_mark = models.IntegerField("Examination Mark", max_length = 3)
	test_mark = models.IntegerField("Class Test Mark" , max_length = 3)
	percentage = models.IntegerField(max_length = 3)
	grade = models.CharField(max_length = 1)

	def __unicode__(self):
		return self.subject

	class Meta:
		db_table = "report content"
		verbose_name = "Report Content"



"""
Adminstaration Customization
"""
class ReportcontentInline(admin.TabularInline):
	model= Report_content
	extra = 8		
class ReportAdmin(admin.ModelAdmin):
	inlines = [ReportcontentInline]
	list_display = ['student_name' , 'course' , 'teacher' , 'date_created']

class ESInline(admin.TabularInline):
	model = Elective_subjects
	extra = 4

class CourseAdmin(admin.ModelAdmin):
	inlines = [ESInline]
	list_display = ['course_name' , 'number_student']
	
admin.site.register(Student)
#admin.site.register(Student_Info)
admin.site.register(Teacher)
#admin.site.register(Teaches)
admin.site.register(Report, ReportAdmin)
#admin.site.register(Report_content)
admin.site.register(Elective_subjects)
admin.site.register(Core_subjects)
admin.site.register(Course , CourseAdmin)
admin.site.register(Subject)
