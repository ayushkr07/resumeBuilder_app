# Generated by Django 3.0.8 on 2020-07-29 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0008_auto_20200729_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='name',
            new_name='school_name',
        ),
    ]
