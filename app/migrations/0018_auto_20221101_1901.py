# Generated by Django 3.2.3 on 2022-11-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='file',
            field=models.FileField(null=True, upload_to='file/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
