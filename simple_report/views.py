from django.http import HttpResponse, HttpResponseRedirect
from models import *
import bform
from form import ReportForm
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt



def recent(request):
	reports = Report.objects.all()
	
	return render_to_response('simple_report/recent.html' , dict(reports = reports))

def detail(request , pk ):
	reports = Report.objects.filter(id = pk)
	subjects = Subject.objects.filter(report = pk)
	return render_to_response('simple_report/detail.html' , dict(reports = reports , pk = pk , subjects = subjects))
	
def report(request , pk):
	""" listing subjects in a report """
	subjects = Subject.objects.filter(report =pk)
	report = Report.objects.get(pk =pk )
	return render_to_response("simple_report/report_detail.html" , dict( subjects = subjects , report = report , pk = pk , name = report.name ))
	

	
	

@csrf_exempt
def add_report(request):
	if request.method == 'GET':
		reportform = bform.ReportForm()
		subjectforms = []
		for i in range(8):
			subjectforms.append(bform.SubjectForm(prefix = 'f%s'%i))
	
	if request.method == "POST":
		reportform = bform.ReportForm(request.POST)
		subjectform = bform.SubjectForm()
		if reportform.is_valid():
			report = reportform.save()
			subjectforms = []
			for i in range(8):
				subjectforms.append(bform.SubjectForm(report = report , prefix = 'f%s'%i , data = request.Post))
			
			for form in subjectforms:
				if form.is_valid():
					form.save()
			return HttpResponseRedirect(report.get_absolute_url())
	
	return render_to_response('simple_report/add_report.html' , dict(reportform = reportform , subjectforms = subjectforms))

