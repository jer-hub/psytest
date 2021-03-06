# Generated by Django 3.2.7 on 2022-04-28 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riasec', '0005_auto_20220428_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('R', 'Realistic'), ('I', 'Investigative'), ('A', 'Artistic'), ('S', 'Social'), ('E', 'Enterprising'), ('C', 'Conventional')], max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('R', 'Realistic'), ('I', 'Investigative'), ('A', 'Artistic'), ('S', 'Social'), ('E', 'Enterprising'), ('C', 'Conventional')], max_length=100)),
            ],
            options={
                'verbose_name': 'RIASEC Test',
                'verbose_name_plural': 'RIASEC Tests',
            },
        ),
        migrations.DeleteModel(
            name='RIASEC_Test',
        ),
        migrations.AlterField(
            model_name='riasec_result',
            name='prediction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='riasec.cluster'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='riasec.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
