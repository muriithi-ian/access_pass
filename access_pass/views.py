from django.shortcuts import render, HttpResponse, redirect
from .forms import DCRulesForm, PersonellDetailsForm, VisitRequestForm, SignNDAForm
from formtools.wizard.views import SessionWizardView

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


class AccessFormView(SessionWizardView):
    template_name = 'access_forms.html'
    form_list = [PersonellDetailsForm, VisitRequestForm]

    def done(self, form_list, **kwargs):
        return render(self.request, 'success.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


def success(request):
    return render(request, 'success.html')
