# Generated by Django 2.2.12 on 2020-06-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20200619_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='gender',
            field=models.BooleanField(default=True),
        ),
    ]
