# Generated by Django 3.2.7 on 2022-04-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riasec', '0008_remove_answer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
