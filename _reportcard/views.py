from django.shortcuts import render_to_response
from models import *
from forms import *


def display_forms(request):
	if request.method == 'GET':
		reportform = ReportForm()
		remark = RemarkForm()
		report_contentforms = []
		for form in range(8):
			report_contentforms.append(Report_contentForm())

	return render_to_response('_reportcard/forms.html' ,dict(rform = reportform , rcform = report_contentforms , remark = remark) )
		
