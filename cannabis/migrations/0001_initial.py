# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-28 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSubstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalTypePatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.AnimalType')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pubmed', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('abstract', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleArticleResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.TextField()),
                ('regimen', models.TextField()),
                ('cell_type', models.TextField()),
                ('side_effect', models.TextField()),
                ('combination', models.TextField()),
                ('human_study_parameters', models.TextField()),
                ('years_min', models.TextField()),
                ('years_max', models.TextField()),
                ('number_of_pations', models.TextField()),
                ('fk_animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.AnimalType')),
                ('fk_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalTrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.TextField()),
                ('clin_study_type', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icd10_field', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseSymptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseSynonyms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('fk_disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('drug_bank', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugActive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_active_substance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.ActiveSubstance')),
                ('fk_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='DrugFormation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='DrugSynonyms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_synonyms', models.TextField()),
                ('fk_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_patient', models.IntegerField(default=0)),
                ('combination', models.TextField()),
                ('years_min', models.CharField(max_length=150)),
                ('years_max', models.CharField(max_length=150)),
                ('fk_gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Gender')),
                ('second_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SideEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='drugformation',
            name='fk_formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Formation'),
        ),
        migrations.AddField(
            model_name='diseasesymptoms',
            name='fk_symptoms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Symptom'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='fk_disease_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Disease'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='fk_drug_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Drug'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='fk_effect_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Effect'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='fk_formation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Formation'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='fk_pation_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.PatientGroup'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='fk_side_effect_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.SideEffect'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Disease'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Drug'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_effect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Effect'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Formation'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Gender'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_patient_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.PatientGroup'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_second_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_condition', to='cannabis.Disease'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_side_effect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.SideEffect'),
        ),
        migrations.AddField(
            model_name='articleresearch',
            name='fk_type_of_research',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.TypeOfResearch'),
        ),
        migrations.AddField(
            model_name='articlearticleresearch',
            name='fk_article_research',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.ArticleResearch'),
        ),
        migrations.AddField(
            model_name='article',
            name='fk_journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.Journal'),
        ),
        migrations.AddField(
            model_name='animaltypepatient',
            name='fk_patient_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis.PatientGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='drugactive',
            unique_together=set([('fk_drug', 'fk_active_substance')]),
        ),
    ]
