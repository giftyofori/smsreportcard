from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from forms import *


def display_forms(request):
	if request.method == 'GET':
		reportform = ReportForm()
		remark = RemarkForm()
		report_contentforms = []
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = '%s'%i))
		ReportFormSet = formset_factory(Report_contentForm ,extra=8)
		formset = ReportFormSet()

	return render_to_response('_reportcard/forms.html' ,dict(rform = reportform , rcform = report_contentforms , remark = remark ,formset = formset) )

@csrf_exempt
def add-report(request):
if request.method == 'GET':
	reportform = ReportForm()
	report_contentforms = []
	for i in range(8):
		report_contentforms.append(Report_contentForm(prefix = '%s'%i))
if request.methos == "POST":
	reportform = ReportForm()
	if  reportform.is_valid():
		report
	
	report_contentforms = []
	for i in range(8):
		report_contentforms.append(Report_contentForm(prefix = '%s'%i))
	for forms in report_contentforms:

	
	
	
	
		
@csrf_exempt
def add_report2(request):
	if request.POST:
		name = request.POST.get('name','')
		date = request.POST.get('date','')
		form = request.POST.get('form','')
		teacher = request.user
		
		print name; print date ; print form; print teacher
	return HttpResponse('check command line')
