from django import forms
from datetime import date

class DCRulesForm(forms.Form):
   pass

class VisitRequestForm(forms.Form):
    PRIORITY_LEVELS = (
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    )

    full_name = forms.CharField(max_length=100, min_length=10, widget=forms.TextInput())
    id_staff_number = forms.CharField(max_length=100,label='ID/Staff Number')
    mobile_number = forms.CharField(max_length=20)
    email_address = forms.EmailField()
    organization_department = forms.CharField(max_length=100, label='Organization/Department')
    equipment_to_be_authorized = forms.CharField(max_length=100, label='Equipment to be authorized')
    reason_for_visit = forms.CharField(max_length=300, widget=forms.Textarea)
    date_of_visit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','min': date.today().strftime('%Y-%m-%d')}, format='%Y-%m-%d'))
    time_of_visit = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))
    priority_level = forms.ChoiceField(choices=PRIORITY_LEVELS, widget=forms.RadioSelect)
    # nature_of_work = forms.CharField(max_length=300, widget=forms.Textarea)
    #action_required_status = forms.CharField(max_length=300, label='Action Required/Status', widget=forms.Textarea)


class SignNDAForm(forms.Form):
   pass


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(), label='Email Address')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('This field is required')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise forms.ValidationError('This field is required')
        return password

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email and not password:
            raise forms.ValidationError('All fields are required')
        return cleaned_data


class RequestForm(forms.Form):
    status= forms.CharField(max_length=100, widget=forms.Select())
    comments= forms.CharField(max_length=300, widget=forms.Textarea)