# Generated by Django 3.2.19 on 2023-07-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0024_apply_job_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_job_tb',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
