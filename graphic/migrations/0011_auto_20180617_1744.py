# Generated by Django 2.0.4 on 2018-06-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0010_auto_20180617_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_info',
            name='num_of_core',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='# Number of Cores'),
        ),
    ]
