# Generated by Django 3.2.19 on 2023-07-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0009_auto_20230703_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_register_tb',
            name='cover',
            field=models.ImageField(upload_to='media/companycover/'),
        ),
        migrations.AlterField(
            model_name='company_register_tb',
            name='logo',
            field=models.ImageField(upload_to='media/companylogo/'),
        ),
    ]