# Generated by Django 4.2.20 on 2025-03-09 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_userprofile_default_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profiles'},
        ),
    ]
