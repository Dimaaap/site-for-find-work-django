# Generated by Django 4.1.5 on 2023-03-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0003_delete_temp_remove_workcriteria_relative_way_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]