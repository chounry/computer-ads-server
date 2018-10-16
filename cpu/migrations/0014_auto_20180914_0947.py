# Generated by Django 2.0.4 on 2018-09-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0013_auto_20180908_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu_info',
            name='series',
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='max_memory',
            field=models.CharField(blank=True, default='---', help_text='Unit: GB or MB', max_length=100),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='proc_num',
            field=models.CharField(help_text='i5-3470 OR 860K OR FX-3202', max_length=30, null=True, verbose_name='Processor Number'),
        ),
    ]
