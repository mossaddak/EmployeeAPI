# Generated by Django 3.2.3 on 2022-10-29 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_employee_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='file',
        ),
    ]
