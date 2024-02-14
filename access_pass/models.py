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
    date_of_visit = models.DateField(auto_now_add=True)
    time_of_visit = models.TimeField(auto_now_add=True)
    priority_level = models.CharField(max_length=100, choices=PRIORITY_LEVELS)
    # nature_of_work = models.TextField()
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

# users= [
#     {'reason_for_visit': 'Fix servers', 'date_of_visit': datetime.date(2024, 2, 6), 'time_of_visit': datetime.time(13, 31, 29, 486331), 'priority_level': 'MEDIUM', 'action_required_status': 'Troubleshooting', 'status': 'PENDING', 'comments': None, 'comments_by': None, 'personnel__full_name': 'Ian Muriithi', 'personnel__id_staff_number': '1234567890', 'personnel__mobile_number': '+254723085151', 'personnel__email_address': 'imuriithiian@gmail.com', 'personnel__organization_department': 'Freelance', 'personnel__primary_personnel': True},
#     {'reason_for_visit': 'Fix servers', 'date_of_visit': datetime.date(2024, 2, 6), 'time_of_visit': datetime.time(13, 31, 29, 486331), 'priority_level': 'MEDIUM', 'action_required_status': 'Troubleshooting', 'status': 'PENDING', 'comments': None, 'comments_by': None, 'personnel__full_name': 'Jack Njihia', 'personnel__id_staff_number': '1234567890', 'personnel__mobile_number': '+254723085151', 'personnel__email_address': 'jack@gmail.com', 'personnel__organization_department': 'Freelance', 'personnel__primary_personnel': False},
#     {'reason_for_visit': 'Update software', 'date_of_visit': datetime.date(2024, 2, 6), 'time_of_visit': datetime.time(13, 32, 2, 678408), 'priority_level': 'HIGH', 'action_required_status': 'Install latest softtware', 'status': 'PENDING', 'comments': None, 'comments_by': None, 'personnel__full_name': 'Mwas Mwas', 'personnel__id_staff_number': '1234567890', 'personnel__mobile_number': '+254723085151', 'personnel__email_address': 'imuriithiian@gmail.com', 'personnel__organization_department': 'Freelance', 'personnel__primary_personnel': True}]

