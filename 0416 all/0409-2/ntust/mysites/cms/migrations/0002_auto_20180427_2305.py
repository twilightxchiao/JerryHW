# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mylife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('englishname', models.CharField(max_length=20)),
                ('age', models.DecimalField(decimal_places=0, max_digits=6)),
                ('birthday', models.CharField(max_length=20)),
                ('constellation', models.CharField(max_length=3)),
                ('likefood', models.CharField(max_length=50)),
                ('likecountry', models.CharField(max_length=50)),
                ('likesong', models.CharField(max_length=50)),
                ('likemovietype', models.CharField(max_length=50)),
                ('things', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
