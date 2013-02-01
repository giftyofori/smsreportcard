from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import *
from models import *
import datetime


"""
DISPLAY THE MAIN PAGE
"""
def main(request):
	return render_to_response('home/main.html',{})



@login_required
def report_detail(request , pk):
	report = Report.objects.filter(id = pk)
	report_content = Report_content.objects.filter(report = pk)
	return render_to_response('_reportcard/report_detail.html', dict(reports = report , pk = pk , subjects = report_content ))

def display_forms(request):
	if request.method == 'GET':
		reportform = ReportForm()
		remark = RemarkForm()
		report_contentforms = []
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = '%s'%i))
		ReportFormSet = formset_factory(Report_contentForm ,extra=8)
		formset = ReportFormSet()

	return render_to_response('_reportcard/add_report.html' ,dict(rform = reportform , rcform = report_contentforms , remark = remark ,formset = formset) )

@login_required
def all_reports(request):
	reports = Report.objects.all()
	return HttpResponse(reports)

@login_required
@csrf_exempt
def add_report(request):
	if request.method == 'GET':
		reportform = ReportForm()
		report_contentforms = []
		time = datetime.datetime.now()		
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = 'f%s'%i))
	if request.method == 'POST':
		reportform = ReportForm(request.POST)
		report_contentforms = Report_contentForm()
		if reportform.is_valid():
			report = reportform.save()
			print 'report object ' , report
			report_contentforms = []
			for i in range(8):
				report_contentforms.append(Report_contentForm(report = report , prefix = 'f%s'%i , data = request.POST ))

			for form in report_contentforms:
				if form.is_valid():
					form.save()
			
			return HttpResponseRedirect(report.get_absolute_url())
	return render_to_response('_reportcard/add_report.html' , dict(rform = reportform , rcform = report_contentforms , time = time))
			
		
		
		

"""

def add_report(request):

	
	reportform = ReportForm()
	if  reportform.is_valid():
		reportform.save()
	
	report_contentforms = []
	for i in range(8):
		report_contentforms.append(Report_contentForm(prefix = '%s'%i))
	for form in report_contentforms:
		if form.is_valid():
			form.save()
	return render_to_response('_reportcard/added.html', dict())

	

	
	
		
@csrf_exempt
def add_report2(request):
	if request.POST:
		name = request.POST.get('name','')
		date = request.POST.get('date','')
		form = request.POST.get('form','')
		teacher = request.user
		
		print name; print date ; print form; print teacher
	return HttpResponse('check command line')
"""
