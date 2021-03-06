# Generated by Django 3.2.7 on 2022-04-28 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riasec', '0006_auto_20220428_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realistic', models.FloatField(default=0)),
                ('investigative', models.FloatField(default=0)),
                ('artistic', models.FloatField(default=0)),
                ('social', models.FloatField(default=0)),
                ('enterprising', models.FloatField(default=0)),
                ('conventional', models.FloatField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('prediction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='riasec.cluster')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_result_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_answer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Riasec_result',
        ),
    ]
