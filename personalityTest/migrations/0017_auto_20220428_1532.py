# Generated by Django 3.2.7 on 2022-04-28 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personalityTest', '0016_auto_20220428_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_answer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_result_user', to=settings.AUTH_USER_MODEL),
        ),
    ]