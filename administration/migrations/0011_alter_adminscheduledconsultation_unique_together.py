# Generated by Django 3.2.7 on 2022-05-22 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_program_code'),
        ('administration', '0010_alter_adminscheduledconsultation_client'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adminscheduledconsultation',
            unique_together={('managed_by', 'client')},
        ),
    ]
