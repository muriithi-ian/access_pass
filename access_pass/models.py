from django.db import models
from django.contrib.auth.models import Group, Permission


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
    primary_personell = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    visit_request_details_id = models.ForeignKey(VisitRequestDetail, on_delete=models.CASCADE)


class CreateGroups:
    if Group.objects.filter(name="officer").exists() is False:
        officer_group = Group.objects.create(name="officer")

    if Group.objects.filter(name="supervisor").exists() is False:
        supervisor_group = Group.objects.create(name='supervisor')

    if Group.objects.filter(name="manager").exists() is False:
        manager_group = Group.objects.create(name='manager')


def ready(self):
    my_models = ['VisitRequestDetail', 'PersonnelDetail']
    read_permission = Permission.objects.get(
        model_codename__in=my_models,
        codename__startswith='can_view',
    )

    write_permission = Permission.objects.get(
        model_codename__in=my_models,
        codename__startswith='can_add',
    )

    edit_permission = Permission.objects.get(
        model_codename__in=my_models,
        codename__startswith='can_change',
    )

    if Group.objects.filter(name="officer").exists() is False:
        officer_group = Group.objects.create(name="officer")
        officer_group.permissions.add(read_permission)
    else:
        officer_group = Group.objects.get(name="officer")
        officer_group.permissions.add(read_permission)

    if Group.objects.filter(name="supervisor").exists() is False:
        supervisor_group = Group.objects.create(name='supervisor')
        supervisor_group.permissions.add([read_permission, write_permission, edit_permission])
    else:
        supervisor_group = Group.objects.get(name="supervisor")
        supervisor_group.permissions.add([read_permission, write_permission, edit_permission])

    if Group.objects.filter(name="manager").exists() is False:
        manager_group = Group.objects.create(name='manager')
        manager_group.permissions.add(read_permission, write_permission, edit_permission)
    else:
        manager_group = Group.objects.get(name="manager")
        manager_group.permissions.add(read_permission, write_permission, edit_permission)

