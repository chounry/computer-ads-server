# Generated by Django 2.0.4 on 2019-04-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0015_auto_20180914_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=400, upload_to='cpu'),
        ),
    ]
