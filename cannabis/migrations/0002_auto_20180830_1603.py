# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-30 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleresearch',
            name='fk_article',
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_article',
            field=models.ManyToManyField(to='cannabis.Article'),
        ),
    ]