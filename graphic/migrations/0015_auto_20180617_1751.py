# Generated by Django 2.0.4 on 2018-06-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0014_auto_20180617_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_info',
            name='model_num',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
