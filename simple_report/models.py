from django.db import models
from django.contrib import admin



class Report(models.Model):
	COURSE = (("BUSINESS","BUSINESS"),("SCIENCE","SCIENCE"))


	name = models.CharField("Student Name",max_length=50)
	course = models.CharField( "Student Cource",choices = COURSE , max_length = 20 , default = COURSE[0][0])
	
	def __unicode(self):
		return self.name
		
	def get_absolute_url(self):
		return '/report/%s/' % self.id
		
		


class Subject(models.Model):
	
	GRADE = (
				("A","Grade A"),
				("B" , "Grade B"),
				("C", "Grade C"),
				("D", "Grade D"),
				("E" ,"Grade E"),
				("F" , "Grade F"),
			)
	
	
	
	s = models.CharField(max_length = 20)
	grade = models.CharField(max_length = 1 , choices = GRADE ,default = GRADE[0][0])
	report = models.ForeignKey(Report)
	
	def __unicode__(self):
		 return self.title
		 
	def save(self):
		self.title = "maths"
		super(Subject , self).save()
	 

'''	
	def create(self):
		core_subjects = ['Eng' , 'Math' , 'Sci' , 'SoS']
		for i in core_subject:
			b= 
'''		

class SubjectInline(admin.TabularInline): 
	model = Subject
	extra = 8
		 
class ReportAdmin(admin.ModelAdmin):
	inlines=[SubjectInline]
	list_display = ["name" , "course"]
	
class SubjectAdmin(admin.ModelAdmin):
	extra = 8
		




admin.site.register(Report , ReportAdmin)		
admin.site.register(Subject , SubjectAdmin)		
		 
		 

