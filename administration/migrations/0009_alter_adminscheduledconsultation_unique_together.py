# Generated by Django 3.2.7 on 2022-05-22 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_alter_adminscheduledconsultation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adminscheduledconsultation',
            unique_together=set(),
        ),
    ]