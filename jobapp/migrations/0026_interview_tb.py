# Generated by Django 3.2.19 on 2023-07-21 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0025_apply_job_tb_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='interview_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=225)),
                ('time', models.CharField(max_length=225)),
                ('require', models.CharField(max_length=225)),
                ('msg', models.CharField(max_length=225)),
                ('loca', models.CharField(max_length=225)),
                ('link', models.CharField(max_length=225)),
                ('aplyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.apply_job_tb')),
            ],
        ),
    ]
