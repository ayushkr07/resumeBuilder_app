# Generated by Django 3.0.8 on 2020-07-29 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0006_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='student',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='student',
            new_name='user',
        ),
    ]
