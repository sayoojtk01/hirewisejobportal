# Generated by Django 3.2.20 on 2023-08-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0036_apply_job_tb_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job_tb',
            name='date',
            field=models.DateField(),
        ),
    ]
