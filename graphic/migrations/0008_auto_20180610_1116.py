# Generated by Django 2.0.4 on 2018-06-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0007_auto_20180526_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_info',
            name='mem_cap',
            field=models.CharField(help_text='Unit: MB', max_length=20, verbose_name='Memory Capacity'),
        ),
    ]
