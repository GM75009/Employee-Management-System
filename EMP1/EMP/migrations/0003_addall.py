# Generated by Django 3.2.16 on 2022-11-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMP', '0002_alter_employeedetail_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('DOB', models.CharField(max_length=50)),
                ('Time', models.TimeField(max_length=50)),
                ('Place', models.CharField(max_length=50)),
            ],
        ),
    ]