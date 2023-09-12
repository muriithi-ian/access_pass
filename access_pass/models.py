from django.db import models

# Create your models here.


class VisitRequestDetails(models.Model):
    PRIORITY_LEVELS = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )

    reason_for_visit = models.TextField()
    date_of_visit = models.DateField()
    time_of_visit = models.TimeField()
    priority_level = models.CharField(max_length=100, choices=PRIORITY_LEVELS)
    date_reported = models.DateField()
    date_resolved = models.DateField()
    nature_of_work = models.TextField()
    action_required_status = models.TextField()
    client_comments = models.TextField()


class PersonnelDetails(models.Model):
    full_name = models.CharField(max_length=100)
    id_staff_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    organization = models.CharField(max_length=100)
    organization_department = models.CharField(max_length=100)
    primary_personell = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    VisitRequestDetails = models.ForeignKey(VisitRequestDetails, on_delete=models.CASCADE)