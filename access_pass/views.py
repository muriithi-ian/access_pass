from django.core import serializers
from django.shortcuts import render, HttpResponse, redirect

from access_pass.models import PersonnelDetail, VisitRequestDetail
from .forms import DCRulesForm, VisitRequestForm, SignNDAForm
from formtools.wizard.views import SessionWizardView
import datetime


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


# form list and templates
FORMS = [("dc_rules", DCRulesForm),
         ("visit_request", VisitRequestForm), ("sign_nda", SignNDAForm)]
TEMPLATES = {"dc_rules": "dc_rules.html",
             'visit_request': 'access_forms.html', "sign_nda": "sign_nda.html"}


class AccessFormView(SessionWizardView):
    current_date = datetime.datetime.now().strftime("%Y %m %d")
    context = {'value': current_date}

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        # print(form_data)

        # save visit request data to database
        reason_for_visit = form_data[1]['reason_for_visit']
        date_of_visit = form_data[1]['date_of_visit']
        time_of_visit = form_data[1]['time_of_visit']
        priority_level = form_data[1]['priority_level']
        action_required_status = form_data[1]['action_required_status']

        # save visit request data to database
        visit_request_detail = VisitRequestDetail(
            reason_for_visit=reason_for_visit, date_of_visit=date_of_visit, time_of_visit=time_of_visit,
            priority_level=priority_level, action_required_status=action_required_status)
        visit_request_detail.save()

        # personell data
        full_name = form_data[1]['full_name']
        id_staff_number = form_data[1]['id_staff_number']
        mobile_number = form_data[1]['mobile_number']
        email_address = form_data[1]['email_address']
        organization_department = form_data[1]['organization_department']
        primary_personell = True
        visit_request_details_id = visit_request_detail

        # save personell data to database
        personnel_detail = PersonnelDetail(full_name=full_name, id_staff_number=id_staff_number,
                                           mobile_number=mobile_number,
                                           email_address=email_address, organization_department=organization_department,
                                           primary_personell=primary_personell,
                                           visit_request_details_id=visit_request_details_id)
        personnel_detail.save()
        # if extra personell data is available

        return render(self.request, 'success.html', {'form_data': form_data})


def success(request):
    return render(request, 'success.html')


def tables(request):
    data = serializers.serialize("json", VisitRequestDetail.objects.all())
    visitors = [
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'Jane Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'John Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Pending'
        },
        {
            'name': 'Jane Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'High',
            'status': 'Approved'
        },
        {
            'name': 'Jane Doe',
            'time': '10:00',
            'date': '12/09/2021',
            'reason': 'Meeting with the manager',
            'priority': 'Low',
            'status': 'Approved'
        }
    ]

    context = {'data': data, 'visitors': visitors}
    return render(request, 'tables.html', context)
