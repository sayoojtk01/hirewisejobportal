# Generated by Django 3.2.19 on 2023-07-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_auto_20230703_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_register_tb1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=225)),
                ('uname', models.CharField(max_length=225)),
                ('cname', models.CharField(max_length=225)),
                ('ctype', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('pinterest', models.CharField(max_length=255)),
                ('dribble', models.CharField(max_length=255)),
                ('behance', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='companylogo/')),
                ('cover', models.ImageField(upload_to='companycover/')),
                ('working', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='company_register_tb',
        ),
    ]
