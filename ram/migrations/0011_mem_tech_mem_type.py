# Generated by Django 2.0.4 on 2018-06-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0010_auto_20180623_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='mem_tech',
            name='mem_type',
            field=models.CharField(default=' ', help_text='eg: SDRAM', max_length=30, null=True),
        ),
    ]
