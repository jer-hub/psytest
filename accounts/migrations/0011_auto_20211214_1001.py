# Generated by Django 3.2.7 on 2021-12-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_delete_adminscheduledtask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_scheduled',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='managed_by',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='scheduled_date',
        ),
    ]
