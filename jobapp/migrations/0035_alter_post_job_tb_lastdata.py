# Generated by Django 3.2.20 on 2023-08-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0034_alter_post_job_tb_lastdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_job_tb',
            name='lastdata',
            field=models.DateField(),
        ),
    ]
