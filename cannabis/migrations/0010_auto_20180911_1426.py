# Generated by Django 2.1 on 2018-09-11 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis', '0009_auto_20180911_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleresearch',
            name='cell_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='combination',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='dosage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_animal_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.AnimalType'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.Disease'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_drug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.Drug'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.Effect'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.Formation'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.Gender'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_patient_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.PatientGroup'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_second_condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_condition', to='cannabis.Disease'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_side_effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.SideEffect'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='fk_type_of_research',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis.TypeOfResearch'),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='human_study_parameters',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='number_of_pations',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='regimen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='side_effect',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='years_max',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articleresearch',
            name='years_min',
            field=models.TextField(blank=True, null=True),
        ),
    ]
