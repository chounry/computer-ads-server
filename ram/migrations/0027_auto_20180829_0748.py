# Generated by Django 2.0.4 on 2018-08-29 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0026_auto_20180721_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory_market',
            name='market',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.Market_info'),
        ),
        migrations.AlterField(
            model_name='memory_market',
            name='memory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ram.Memory_info'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='form_factor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ram.Form_factor'),
        ),
    ]
