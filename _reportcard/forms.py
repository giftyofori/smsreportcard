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



class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = "" ,required = False ,initial = "Marths" , widget=forms.TextInput(attrs={'class':'subject'}))
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int ,required = False , initial =23,widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" ,required = False , initial = 23 , widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "",initial =100 , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform'}))
	grade = forms.CharField(max_length = 1 , required = False , label = "" ,initial = "A",widget=forms.TextInput(attrs={'class':'grade','id':'grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def save(self):
		
		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = self.cleaned_data['percentage'] , grade = self.cleaned_data['grade'])
		report_content.save()

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")
