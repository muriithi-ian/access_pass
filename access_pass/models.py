from django.db import models

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
    nature_of_work = models.TextField()
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