# Generated by Django 2.0.4 on 2018-06-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0016_auto_20180617_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api_supp',
            options={'verbose_name': 'API Support'},
        ),
        migrations.AlterModelOptions(
            name='gpu_brand',
            options={'verbose_name': 'GPU Brand'},
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='boost_clock',
            field=models.PositiveIntegerField(blank=True, help_text='Unit :MHz', null=True),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='core_clock',
            field=models.PositiveIntegerField(blank=True, help_text='Unit :MHz', null=True),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='name',
            field=models.CharField(blank=True, help_text='Do not include Manufactur Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]