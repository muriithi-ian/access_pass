from django import forms


class DCRulesForm(forms.Form):
   pass

class VisitRequestForm(forms.Form):
    PRIORITY_LEVELS = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )

    full_name = forms.CharField(max_length=100, widget=forms.TextInput())
    id_staff_number = forms.CharField(max_length=100,label='ID/Staff Number' )
    mobile_number = forms.CharField(max_length=20)
    email_address = forms.EmailField()
    organization_department = forms.CharField(max_length=100, label='Organization/Department')
    reason_for_visit = forms.CharField(max_length=300, widget=forms.Textarea)
    date_of_visit = forms.DateField(widget=forms.SelectDateWidget())
    time_of_visit = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    priority_level = forms.ChoiceField(choices=PRIORITY_LEVELS, widget=forms.RadioSelect)
    nature_of_work = forms.CharField(max_length=300, widget=forms.Textarea)
    action_required_status = forms.CharField(max_length=300, label='Action Required/Status', widget=forms.Textarea)


class SignNDAForm(forms.Form):
   pass