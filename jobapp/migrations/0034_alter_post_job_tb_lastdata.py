# Generated by Django 3.2.20 on 2023-08-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0033_post_job_tb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_job_tb',
            name='lastdata',
            field=models.DateField(max_length=225),
        ),
    ]