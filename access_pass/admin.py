from django.contrib import admin
from .models import VisitRequestDetail, PersonnelDetail

# Register your models here and show fields.
# admin.site.register(PersonnelDetail, list_display=['full_name', 'id_staff_number', 'mobile_number',
admin.site.register(PersonnelDetail, list_display=[
                    'id', 'full_name', 'id_staff_number', 'mobile_number', 'email_address', 'organization_department', 'primary_personell', 'created_on', 'visit_request_details_id'])

admin.site.register(VisitRequestDetail, list_display=[
                    'id', 'reason_for_visit', 'date_of_visit', 'time_of_visit', 'priority_level', 'nature_of_work', 'action_required_status'])
