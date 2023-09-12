from django import forms
from .models import VisitRequestDetails, PersonnelDetails


class DCRulesForm(forms.Form):
    pass

class PersonellDetailsForm(forms.ModelForm):
    PRIMARY_PERSONELL = (
        (True, "Yes"),
        (False, 'No'),
    )

    primary_personell = forms.ChoiceField(choices=PRIMARY_PERSONELL, widget=forms.RadioSelect)


    class Meta:
        model = PersonnelDetails
        fields = ['full_name', 'id_staff_number', 'mobile_number', 'email_address', 'organization', 'organization_department',]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_staff_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_department': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VisitRequestForm(forms.ModelForm):
    class Meta:
        model = VisitRequestDetails
        fields = ['reason_for_visit', 'date_of_visit', 'time_of_visit', 'priority_level', 'date_reported', 'date_resolved', 'nature_of_work', 'action_required_status', 'client_comments']
        widgets = {
            'reason_for_visit': forms.Textarea(attrs={'class': 'form-control'}),
            'date_of_visit': forms.DateInput(attrs={'class': 'form-control'}),
            'time_of_visit': forms.TimeInput(attrs={'class': 'form-control'}),
            'priority_level': forms.Select(attrs={'class': 'form-control'}),
            'date_reported': forms.DateInput(attrs={'class': 'form-control'}),
            'date_resolved': forms.DateInput(attrs={'class': 'form-control'}),
            'nature_of_work': forms.Textarea(attrs={'class': 'form-control'}),
            'action_required_status': forms.Textarea(attrs={'class': 'form-control'}),
            'client_comments': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SignNDAForm(forms.Form):
    pass
