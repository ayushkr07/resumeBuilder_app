# Generated by Django 3.0.8 on 2020-07-29 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0014_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_itle',
            new_name='project_title',
        ),
    ]
