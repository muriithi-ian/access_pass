# Generated by Django 4.2.4 on 2023-09-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_pass', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personneldetail',
            old_name='VisitRequestDetail',
            new_name='visit_request_details_id',
        ),
        migrations.RemoveField(
            model_name='personneldetail',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='visitrequestdetail',
            name='client_comments',
        ),
        migrations.RemoveField(
            model_name='visitrequestdetail',
            name='date_reported',
        ),
        migrations.RemoveField(
            model_name='visitrequestdetail',
            name='date_resolved',
        ),
        migrations.AlterField(
            model_name='personneldetail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personneldetail',
            name='organization_department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personneldetail',
            name='primary_personell',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='date_of_visit',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='time_of_visit',
            field=models.TimeField(auto_now_add=True),
        ),
    ]