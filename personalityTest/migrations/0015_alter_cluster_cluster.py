# Generated by Django 3.2.7 on 2022-04-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalityTest', '0014_remove_result_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='cluster',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
