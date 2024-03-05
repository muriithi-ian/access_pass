from django.contrib import admin
from .models import VisitRequestDetail, PersonnelDetail, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmmin
from django.utils.translation import gettext_lazy as _


# Register your models here and show fields.
# admin.site.register(PersonnelDetail, list_display=['full_name', 'id_staff_number', 'mobile_number',
admin.site.register(PersonnelDetail, list_display=[
                    'id', 'full_name', 'id_staff_number', 'mobile_number', 'email_address', 'organization_department', 'primary_personnel', 'created_on', 'visit_request_details_id'])

admin.site.register(VisitRequestDetail, list_display=[
                    'id', 'reason_for_visit', 'date_of_visit', 'time_of_visit', 'priority_level',  'action_required_status', 'status', 'created_on', 'comments', 'comments_by'])


class UserAdmin(BaseUserAdmmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ['email', 'is_officer', 'is_supervisor', 'is_manager', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'username']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']


admin.site.register(User, UserAdmin)
admin.site.register
