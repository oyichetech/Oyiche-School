# Generated by Django 5.1.4 on 2025-01-06 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyiche_schMGT', '0004_academicsession_school_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentenrollment',
            name='school_academic_information',
        ),
        migrations.AddField(
            model_name='academicsession',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='academicterm',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='academicterm',
            name='school_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_academic_term', to='oyiche_schMGT.schoolinformation'),
        ),
        migrations.AddField(
            model_name='studentenrollment',
            name='academic_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_academic_session', to='oyiche_schMGT.academicsession'),
        ),
        migrations.AddField(
            model_name='studentenrollment',
            name='academic_term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_academic_term', to='oyiche_schMGT.academicterm'),
        ),
        migrations.AlterField(
            model_name='academicsession',
            name='school_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_academic_session', to='oyiche_schMGT.schoolinformation'),
        ),
        migrations.DeleteModel(
            name='SchoolAcademicInformation',
        ),
    ]
