# Generated by Django 2.1 on 2018-09-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis', '0019_auto_20180913_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='fk_article_research',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis.ArticleResearch'),
        ),
        migrations.AlterField(
            model_name='article',
            name='fk_author',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis.Author'),
        ),
    ]
