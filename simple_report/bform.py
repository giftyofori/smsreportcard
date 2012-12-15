from django import forms
from django.forms import ModelForm
from models import *


class ReportForm(ModelForm):
	class Meta:
		model = Report
		
class SubjectForm(forms.Form):
	subject = forms.CharField(max_length = 25 )
	
	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(SubjectForm , self).__init__(*args, **kwargs)
		
	def save(self):
		subject = models.Subject(report = self.report , subject = self.clean_data['subject'])
		subject.put()



'''

class ChoiceForm(forms.Form):
    choice = forms.CharField(max_length = 100, widget = forms.Textarea)

    def __init__(self , poll = None , *args, **kwargs):
        self.poll = poll
        super(ChoiceForm, self).__init__(*args,**kwargs)
		
    def save(self):
        choice = models.Choice(poll = self.poll,choice = self.clean_data['choice'])	
        chocie.put()
		
'''