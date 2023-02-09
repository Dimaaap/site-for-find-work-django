# Generated by Django 4.1.5 on 2023-02-09 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0010_alter_jobseekerprofileinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerprofileinfo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
    ]
