# Generated by Django 4.2.4 on 2024-02-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_pass', '0004_visitrequestdetail_modified_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='date_of_visit',
            field=models.DateField(default='2024-02-19'),
        ),
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='time_of_visit',
            field=models.TimeField(default='09:46'),
        ),
    ]