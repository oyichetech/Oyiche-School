# Generated by Django 5.1.4 on 2025-01-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyiche_schMGT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolclasses',
            old_name='school',
            new_name='school_info',
        ),
        migrations.RemoveField(
            model_name='schoolclasses',
            name='student_class',
        ),
        migrations.AddField(
            model_name='schoolclasses',
            name='class_name',
            field=models.CharField(default='', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
