# Generated by Django 3.2.3 on 2022-10-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_employee_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='file',
            field=models.FileField(null=True, upload_to='file/'),
        ),
    ]
