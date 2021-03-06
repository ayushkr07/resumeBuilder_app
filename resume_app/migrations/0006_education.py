# Generated by Django 3.0.8 on 2020-07-28 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume_app', '0005_auto_20200728_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=30)),
                ('field', models.CharField(max_length=70)),
                ('percentage_or_cg', models.CharField(max_length=10)),
                ('graduation_year', models.CharField(max_length=8)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
