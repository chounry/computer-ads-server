# Generated by Django 2.0.4 on 2018-06-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0008_auto_20180617_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expansion_slot',
            name='pin',
            field=models.CharField(blank=True, default=' ', max_length=10),
        ),
    ]
