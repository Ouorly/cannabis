# Generated by Django 2.1 on 2018-09-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis', '0005_auto_20180831_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='fk_author',
            field=models.ManyToManyField(to='cannabis.Author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
