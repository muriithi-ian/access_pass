from django.shortcuts import render, HttpResponse, redirect
from .forms import DCRulesForm, VisitRequestForm, SignNDAForm
from formtools.wizard.views import SessionWizardView

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
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        print(form_data)
        return render(self.request, 'success.html', {'form_data': form_data})


def success(request):
    return render(request, 'success.html')
