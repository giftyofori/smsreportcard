from django import forms
import datetime
errormsg_text = {'required' :'Field is required'}
errormsg_int = {'required': 'Field is Required' , 'invalid':'Invalid Entry' ,'max_value':'Maximum Value Exceeded' , 'min_value':'Minivalue Required'}

class ReportForm(forms.Form):
	date = forms.DateField(initial=datetime.date.today)
	name = forms.CharField(max_length = 100)
	form = forms.CharField(max_length = 5 , label = "SHS")
	teacher= forms.CharField(max_length = 100 , initial = 'request.user')
	

class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = "")
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int)
	text_mark = forms.IntegerField(max_value =  200 ,label = "")
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "")
	grade = forms.CharField(max_length = 1 , required = False , label = "")
	
class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea ,initial = "Good Work More Room for Improvement")
