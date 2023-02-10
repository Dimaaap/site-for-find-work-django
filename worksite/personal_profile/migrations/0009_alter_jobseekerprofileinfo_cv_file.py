# Generated by Django 4.1.5 on 2023-02-07 22:13

from django.db import migrations, models
import personal_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0008_alter_jobseekerprofileinfo_cv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerprofileinfo',
            name='cv_file',
            field=models.FileField(upload_to='cvs/%Y/%m/%d', validators=[personal_profile.models.validate_file_extension]),
        ),
    ]