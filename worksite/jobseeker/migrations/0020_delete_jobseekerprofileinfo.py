# Generated by Django 4.1.5 on 2023-01-25 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0019_remove_jobseekerprofileinfo_skype_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobseekerProfileInfo',
        ),
    ]
