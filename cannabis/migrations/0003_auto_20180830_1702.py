# Generated by Django 2.1 on 2018-08-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis', '0002_auto_20180830_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleresearch',
            name='fk_article',
        ),
        migrations.AddField(
            model_name='article',
            name='fk_article_research',
            field=models.ManyToManyField(to='cannabis.ArticleResearch'),
        ),
    ]
