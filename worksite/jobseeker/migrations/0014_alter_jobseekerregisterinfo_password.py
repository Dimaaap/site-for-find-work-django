# Generated by Django 4.1.5 on 2023-01-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0013_alter_jobseekerregisterinfo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerregisterinfo',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
