# Generated by Django 2.0.4 on 2018-07-01 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0024_auto_20180701_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory_info',
            name='isECC',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='---', max_length=3),
        ),
        migrations.AlterField(
            model_name='pin',
            name='form_factor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ram.Form_factor'),
        ),
    ]