# Generated by Django 4.2.4 on 2023-10-18 22:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "access_pass",
            "0002_rename_visitrequestdetail_personneldetail_visit_request_details_id_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visitrequestdetail",
            name="nature_of_work",
        ),
    ]