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
    id = models.AutoField(primary_key=True)
    reason_for_visit = models.TextField()
    date_of_visit = models.DateField(auto_now_add=True)
    time_of_visit = models.TimeField(auto_now_add=True)
    priority_level = models.CharField(max_length=100, choices=PRIORITY_LEVELS)
    # nature_of_work = models.TextField()
    action_required_status = models.TextField()


class PersonnelDetail(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    id_staff_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    organization_department = models.CharField(max_length=100, null=True)
    primary_personnel = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    visit_request_details_id = models.ForeignKey(VisitRequestDetail, on_delete=models.CASCADE, related_name='personnel')


class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True, error_messages={'unique': _('A user with that email already exists.')})
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return "{}".format(self.email)


class UserGroups():
    if Group.objects.filter(name="officer").exists() is False:
        Group.objects.create(name="officer")

    if Group.objects.filter(name="supervisor").exists() is False:
        Group.objects.create(name='supervisor')

    if Group.objects.filter(name="manager").exists() is False:
        Group.objects.create(name='manager')


