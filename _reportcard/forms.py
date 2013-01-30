from django import forms
from django.forms import ModelForm
import datetime
from django.forms.widgets import Select
from models import *
from tweak import subjectstuple
errormsg_text = {'required' :'Field is required'}
errormsg_int = {'required': 'Field is Required' , 'invalid':'Invalid Entry' ,'max_value':'Maximum Value Exceeded' , 'min_value':'Minivalue Required'}


class ReportForm(ModelForm):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	student_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'inputstyle'}))
	form = forms.ChoiceField(widget=forms.Select, choices=FORMS ,initial = "")
	class Meta:
		model = Report



class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = ""  ,initial = "Marths" , widget=forms.TextInput(attrs={'class':'subject'}))
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int , initial =23,widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" ,initial =30, widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "",initial =100 , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform'}))
	grade = forms.CharField(max_length = 1 , required = False , label = "" ,initial = "A",widget=forms.TextInput(attrs={'class':'grade','id':'grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def save(self):
		_exam_mark = self.cleaned_data['exam_mark']
		_test_mark = self.cleaned_data['test_mark']
		print '70 % of exam mark ' + str(_exam_mark) +' is '  + str(int(_exam_mark * 0.7))
		print '30 % of test mark ' + str(_test_mark) +' is ' + str(int(_test_mark ))
		percent = int(round((_exam_mark * 0.7) + (_test_mark * 1)))
		if percent >= 80:
			grade = "A"
		else:
			grade = "B"
		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = percent, grade = grade)
		report_content.save()

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")


"""

class ReportForm(forms.Form):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	date_created = forms.DateField(initial=datetime.date.today)
	student_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'size':'50','class':'inputstyle'}))
	course = forms.CharField(max_length = 50)
	form = forms.ChoiceField(widget=forms.Select, choices=FORMS)
	teacher= forms.CharField(max_length = 100 , initial = 'request.user')
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")

	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(forms.Form, self).__init__(*args, **kwargs)

	def save(self):
		report = Report(student_name = self.cleaned_data['student_name'] , date_created = self.cleaned_data['date_created'] , course = self.cleaned_data['course'] , form = self.cleaned_data['form'] , teacher = self.cleaned_data['teacher'] , remark = self.cleaned_data['remark'])
		report.save()
"""	


'''
class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = ""  ,initial = "Marths" , widget=forms.TextInput(attrs={'class':'subject'}))
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int , initial =23,widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" , widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "",initial =100 , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform'}))
	grade = forms.CharField(max_length = 1 , required = False , label = "" ,initial = "A",widget=forms.TextInput(attrs={'class':'grade','id':'grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def grade(self):
		pass
	
	def save(self):
		_exam_mark = self.cleaned_data['exam_mark']
		_test_mark = self.cleaned_data['test_mark']
		print '70 % of exam mark ' + str(_exam_mark) +' is '  + str(int(_exam_mark * 0.7))
		print '30 % of test mark ' + str(_test_mark) +' is ' + str(int(_test_mark ))
		percent = int(round((_exam_mark * 0.7) + (_test_mark * 1)))
		#calculate grade from percentage
		if percent in range(79,100):

		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = percent, grade = self.cleaned_data['grade'])
		report_content.save()

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")


"""
Auto fill form section 
"""


class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = ""  ,initial = "Marths" , widget=forms.TextInput(attrs={'class':'subject'}))
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int , initial =23,widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" , widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "",initial =100 , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform'}))
	grade = forms.CharField(max_length = 1 , required = False , label = "" ,initial = "A",widget=forms.TextInput(attrs={'class':'grade','id':'grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def save(self):
		_exam_mark = self.cleaned_data['exam_mark']
		_test_mark = self.cleaned_data['test_mark']
		print '70 % of exam mark ' + str(_exam_mark) +' is '  + str(int(_exam_mark * 0.7))
		print '30 % of test mark ' + str(_test_mark) +' is ' + str(int(_test_mark ))
		percent = int(round((_exam_mark * 0.7) + (_test_mark * 1)))
		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = percent, grade = self.cleaned_data['grade'])
		report_content.save()

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")


'''
