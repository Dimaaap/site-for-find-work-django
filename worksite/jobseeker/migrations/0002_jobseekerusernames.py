# Generated by Django 4.1.5 on 2023-01-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobseekerUsernames',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40, unique=True)),
            ],
        ),
    ]
