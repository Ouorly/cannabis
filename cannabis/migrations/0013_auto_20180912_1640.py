# Generated by Django 2.1 on 2018-09-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis', '0012_auto_20180912_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
