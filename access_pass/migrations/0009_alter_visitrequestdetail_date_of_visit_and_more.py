# Generated by Django 4.2.4 on 2024-10-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_pass', '0008_alter_visitrequestdetail_time_of_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='date_of_visit',
            field=models.DateField(default='2024-10-11'),
        ),
        migrations.AlterField(
            model_name='visitrequestdetail',
            name='time_of_visit',
            field=models.TimeField(default='12:42'),
        ),
    ]
