# Generated by Django 2.0.4 on 2018-09-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0025_auto_20180829_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='graphic'),
        ),
    ]