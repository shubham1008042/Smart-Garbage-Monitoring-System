# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-01 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_auto_20190430_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='c_details',
            name='C_D_id',
        ),
        migrations.RemoveField(
            model_name='trashcan1',
            name='T_C_id',
        ),
        migrations.RemoveField(
            model_name='trashcan1',
            name='T_D_id',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='C_Details',
        ),
        migrations.DeleteModel(
            name='D_Details',
        ),
        migrations.DeleteModel(
            name='Trashcan1',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
