# Generated by Django 4.2.4 on 2024-02-14 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('access_pass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitrequestdetail',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='visitrequestdetail',
            name='comments_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='visitrequestdetail',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitrequestdetail',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=100),
        ),
    ]