# Generated by Django 2.0.4 on 2018-06-10 04:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0004_mainboard_info_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainboard_info',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
