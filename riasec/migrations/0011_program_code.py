# Generated by Django 3.2.7 on 2022-05-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riasec', '0010_offeredprogram_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='code',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
