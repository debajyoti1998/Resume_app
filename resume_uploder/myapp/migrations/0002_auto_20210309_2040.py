# Generated by Django 3.1.7 on 2021-03-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='DOB',
            field=models.CharField(max_length=20),
        ),
    ]
