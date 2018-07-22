# Generated by Django 2.0.4 on 2018-06-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0003_auto_20180610_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory_info',
            name='capacity',
            field=models.PositiveSmallIntegerField(help_text='Unit: GB'),
        ),
        migrations.AlterField(
            model_name='memory_info',
            name='fr',
            field=models.PositiveIntegerField(help_text='Unit: MHz', verbose_name='Frequency'),
        ),
        migrations.AlterField(
            model_name='memory_info',
            name='mem_speed',
            field=models.CharField(help_text='Put the unit BY ourselve, Unit: MHz | MB/s', max_length=50, verbose_name='Memory Speed'),
        ),
        migrations.AlterField(
            model_name='memory_info',
            name='model_num',
            field=models.CharField(blank=True, default='---', max_length=100, verbose_name='Item Model Number'),
        ),
        migrations.AlterField(
            model_name='memory_info',
            name='moduel_name',
            field=models.CharField(blank=True, default='---', max_length=50, verbose_name='Moduel Name'),
        ),
    ]
