# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-01 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190501_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=11)),
                ('Reg_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
