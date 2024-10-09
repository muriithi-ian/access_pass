import datetime

from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class VisitRequestDetail(models.Model):
    PRIORITY_LEVELS = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )
    VISIT_STATUS = (
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    )
    id = models.AutoField(primary_key=True)
    reason_for_visit = models.TextField()
    date_of_visit = models.DateField(default= datetime.datetime.now().strftime("%Y-%m-%d"))
    time_of_visit = models.TimeField(default= datetime.datetime.now().strftime("%H:%M"))
    priority_level = models.CharField(max_length=100, choices=PRIORITY_LEVELS)
    action_required_status = models.TextField()
    status = models.CharField(max_length=100, choices=VISIT_STATUS, default='PENDING')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(null=True, blank=True)
    comments_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='visit_comments', null=True, blank=True)

class PersonnelDetail(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    id_staff_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    organization_department = models.CharField(max_length=100, null=True)
    equipment_to_be_authorized = models.CharField(max_length=100, null=True)
    primary_personnel = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    visit_request_details_id = models.ForeignKey(VisitRequestDetail, on_delete=models.CASCADE, related_name='personnel')


class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True, error_messages={'unique': _('A user with that email already exists.')})
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_officer = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return "{}".format(self.email)

