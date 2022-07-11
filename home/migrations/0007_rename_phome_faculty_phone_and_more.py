# Generated by Django 4.0.4 on 2022-06-08 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_faculty_phome_student_phome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='phome',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='phome',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 9, 0, 56, 58, 722036)),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 9, 0, 56, 58, 722036)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 9, 0, 56, 58, 723033)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 9, 0, 56, 58, 723033)),
        ),
    ]