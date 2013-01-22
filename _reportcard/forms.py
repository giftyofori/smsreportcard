from django import forms
import datetime
from django.forms.widgets import Select
errormsg_text = {'required' :'Field is required'}
errormsg_int = {'required': 'Field is Required' , 'invalid':'Invalid Entry' ,'max_value':'Maximum Value Exceeded' , 'min_value':'Minivalue Required'}

class ReportForm(forms.Form):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	date = forms.DateField(initial=datetime.date.today)
	name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'size':'50','class':'inputstyle'}))
	form = forms.ChoiceField(widget=forms.Select, choices=FORMS)
	teacher= forms.CharField(max_length = 100 , initial = 'request.user')
	

class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = "" ,required = False)
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int ,required = False)
	text_mark = forms.IntegerField(max_value =  200 ,label = "" ,required = False)
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "")
	grade = forms.CharField(max_length = 1 , required = False , label = "")
	
class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")
