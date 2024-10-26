import csv
from django.core import serializers
import json
from openpyxl import Workbook # type: ignore

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from access_pass.models import PersonnelDetail, VisitRequestDetail
from .forms import DCRulesForm, VisitRequestForm, SignNDAForm, SignInForm, RequestForm
from formtools.wizard.views import SessionWizardView
import datetime


# Create your views here.

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('applicants')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('signin')

    else:
        form = SignInForm()
        return render(request, 'signin.html', {form: form})


def signout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('signin')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    notifications = 0
    if request.user.is_authenticated:
        notifications = VisitRequestDetail.objects.filter(status='PENDING').count()
    return render(request, 'home.html', {'notifications': notifications})


# form list and templates
FORMS = [("dc_rules", DCRulesForm),
         ("visit_request", VisitRequestForm), ("sign_nda", SignNDAForm)]
TEMPLATES = {"dc_rules": "dc_rules.html",
             'visit_request': 'access_forms.html', "sign_nda": "sign_nda.html"}


#  Get data from step 1 and add to context
def get_reason_for_visit_data(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('visit_request') or {}
    return cleaned_data


class AccessFormView(SessionWizardView):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # initial_dict = {
    #     'visit_request': {'date_of_visit': datetime.datetime.now().strftime("%d/%m/%Y"), 'time_of_visit': datetime.datetime.now().strftime("%H:%M")},
    # }

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    # update context data
    def get_context_data(self, form, **kwargs):
        context = super(AccessFormView, self).get_context_data(form=form, **kwargs)
        context.update({'visit_data': get_reason_for_visit_data(self)})
        return context

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]

        # save visit request data to database
        reason_for_visit = form_data[1]['reason_for_visit']
        date_of_visit = form_data[1]['date_of_visit']
        time_of_visit = form_data[1]['time_of_visit']
        priority_level = form_data[1]['priority_level']

        # save visit request data to database
        visit_request_detail = VisitRequestDetail(
            reason_for_visit=reason_for_visit, date_of_visit=date_of_visit, time_of_visit=time_of_visit,
            priority_level=priority_level)
        visit_request_detail.save()

        # personnel data
        full_name = form_data[1]['full_name']
        id_staff_number = form_data[1]['id_staff_number']
        mobile_number = form_data[1]['mobile_number']
        email_address = form_data[1]['email_address']
        organization_department = form_data[1]['organization_department']
        equipment_to_be_authorized = form_data[1]['equipment_to_be_authorized']
        primary_personnel = True
        visit_request_details_id = visit_request_detail

        # save personnel data to database
        personnel_detail = PersonnelDetail(full_name=full_name, id_staff_number=id_staff_number,
                                           mobile_number=mobile_number,
                                           email_address=email_address, organization_department=organization_department,
                                           equipment_to_be_authorized=equipment_to_be_authorized,
                                           primary_personnel=primary_personnel,
                                           visit_request_details_id=visit_request_details_id)
        personnel_detail.save()
        # if extra personnel data is available
        if 'extra_personnel' in form_data[1]:
            for personnel in form_data[1]['extra_personnel']:
                full_name = personnel['full_name']
                id_staff_number = personnel['id_staff_number']
                mobile_number = personnel['mobile_number']
                email_address = personnel['email_address']
                organization_department = personnel['organization_department']
                equipment_to_be_authorized = personnel['equipment_to_be_authorized']
                primary_personnel = False
                visit_request_details_id = visit_request_detail

                # save personnel data to database
                personnel_detail = PersonnelDetail(full_name=full_name, id_staff_number=id_staff_number,
                                                   mobile_number=mobile_number,
                                                   email_address=email_address, organization_department=organization_department,
                                                   equipment_to_be_authorized=equipment_to_be_authorized,
                                                   primary_personnel=primary_personnel,
                                                   visit_request_details_id=visit_request_details_id)
                personnel_detail.save()
        return render(self.request, 'success.html', {'form_data': form_data})


def success(request):
    if request.user.is_authenticated:
        notifications = VisitRequestDetail.objects.filter(status='PENDING').count()
        return render(request, 'success.html', {'notifications': notifications})
    return render(request, 'success.html')


def tables(request, filter='all'):
    if not request.user.is_authenticated:
        return redirect('signin')
    
     # Get the start and end dates from the GET parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    #Initialize the base queryset
    visits = VisitRequestDetail.objects.all()

    if filter == 'pending':
        visits = VisitRequestDetail.objects.filter(status='PENDING')
    elif filter == 'approved':
        visits = VisitRequestDetail.objects.filter(status='APPROVED')
    elif filter == 'rejected':
        visits = VisitRequestDetail.objects.filter(status='REJECTED')

    notifications = VisitRequestDetail.objects.filter(status='PENDING').count()

     # Apply the date range filter if both start and end dates are provided
    if start_date and end_date:
        # Convert the string dates to datetime objects
        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            visits = visits.filter(date_of_visit__range=[start_date, end_date])
        except ValueError:
            # Handle incorrect date format
            pass

    for visit in visits:
        visit.personnel.set(PersonnelDetail.objects.filter(
            visit_request_details_id=visit.id).only('full_name', 'id_staff_number', 'mobile_number', 'email_address',
                                                    'organization_department', 'equipment_to_be_authorized', 'primary_personnel'))

    data = visits.values(
        'id', 'reason_for_visit', 'date_of_visit', 'time_of_visit', 'priority_level', 'status', 'comments', 'comments_by', 'personnel__full_name',
        'personnel__id_staff_number',
        'personnel__mobile_number', 'personnel__email_address',
        'personnel__organization_department', 'personnel__equipment_to_be_authorized', 'personnel__primary_personnel'
    )
    data = list(data)

    context = {'visits': data, 'notifications': notifications, 'start_date': start_date, 'end_date': end_date}
    return render(request, 'tables.html', context)

def download_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Initialize the base queryset
    visits = VisitRequestDetail.objects.all()

    # Apply the date range filter if both start and end dates are provided
    if start_date and end_date:
        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            visits = visits.filter(date_of_visit__range=[start_date, end_date])
        except ValueError:
            # Handle incorrect date format
            pass

     # Create an Excel response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="request_report.xlsx"'
    
    # Create a Workbook
    workbook = Workbook()
    sheet = workbook.active

    # Write header
    sheet.append(['Full Name', 'ID Number', 'Email', 'Organization', 'Priority Level', 'Date of Visit', 'Reason for Visit', 'Status'])

    # Write the data rows
    for req in visits:
        personnel_list = req.personnel.all()  # Get all personnel related to this visit request
        for personnel in personnel_list:
            sheet.append([
                personnel.full_name,
                personnel.id_staff_number,
                personnel.email_address,
                personnel.organization_department,
                req.priority_level,
                req.date_of_visit.strftime('%Y-%m-%d'),
                req.reason_for_visit,
                req.status
            ])
    workbook.save(response)        
    return response

def visit_request(request, visit_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        visit = VisitRequestDetail.objects.get(id=visit_id)
        visit.status = request.POST['status']
        visit.comments = request.POST['comments']
        visit.comments_by = request.user
        visit.modified_on = datetime.datetime.now()
        visit.save()
        return redirect('applicants')

    visit = VisitRequestDetail.objects.get(id=visit_id)
    personnel = PersonnelDetail.objects.filter(visit_request_details_id=visit_id)    

    personnel = personnel.values(
        'id', 'full_name', 'id_staff_number', 'mobile_number', 'email_address',
        'organization_department', 'equipment_to_be_authorized', 'primary_personnel'
    )
    form = RequestForm()

    notifications = VisitRequestDetail.objects.filter(status='PENDING').count()
    context = {'visit': visit, 'personnel': personnel, 'form': form, 'notifications': notifications}
    return render(request, 'visit_request.html', context)


def print_nda(request, visit_id):
    if not request.user.is_authenticated:
        return redirect('signin')

    visit = VisitRequestDetail.objects.get(id=visit_id)
    personnel = PersonnelDetail.objects.filter(visit_request_details_id=visit_id, primary_personnel=True).first()

    visit_data = {
        'date_of_visit': visit.date_of_visit,
        'organization_department': personnel.organization_department,
        'equipment_to_be_authorized': personnel.equipment_to_be_authorized,
        'reason_for_visit': visit.reason_for_visit,
        'full_name': personnel.full_name,
        'email_address': personnel.email_address,
        'mobile_number': personnel.mobile_number,
        'reason_for_visit': visit.reason_for_visit,
    }
    context = {'visit_data': visit_data}


    return render(request, 'print_nda.html' , context)