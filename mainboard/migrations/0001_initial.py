# Generated by Django 2.0.4 on 2018-05-26 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpu', '0001_initial'),
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chipset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Expansion_connector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='eg: PCI or PCIe or ...', max_length=30)),
                ('version', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Expansion_slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=10)),
                ('expansion_conn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainboard.Expansion_connector')),
            ],
        ),
        migrations.CreateModel(
            name='Form_factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desctiption', models.CharField(max_length=50, verbose_name='Form Factor')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mainboard_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cpu_des', models.TextField(max_length=300, verbose_name='CPU Description')),
                ('size', models.CharField(help_text='30.5cm x 24.4cm', max_length=250)),
                ('storage_des', models.TextField(blank=True, max_length=500, null=True, verbose_name='Storage Description')),
                ('multi_gpu_des', models.TextField(blank=True, null=True, verbose_name='Multi GPU')),
                ('memmory_des', models.TextField(max_length=500, verbose_name='Memory Description')),
                ('rear_panel_des', models.TextField(max_length=350, verbose_name='Rear Panel Description')),
                ('expand_slot_des', models.TextField(max_length=500, verbose_name='Expansion Slot Description')),
                ('audio_des', models.TextField(max_length=300, verbose_name='Audio Description')),
                ('interal_des', models.TextField(max_length=1000, verbose_name='Interal I\\O Connector')),
                ('onboard_gpu_des', models.TextField(blank=True, max_length=400, null=True, verbose_name='On Board GPU')),
                ('chipset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainboard.Chipset')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainboard.Company')),
                ('expan_slot', models.ManyToManyField(to='mainboard.Expansion_slot', verbose_name='Mainbaord Expansion Slot')),
                ('form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainboard.Form_factor')),
                ('socket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpu.Socket_type')),
            ],
        ),
        migrations.CreateModel(
            name='Mainboard_market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=2000)),
                ('prize', models.DecimalField(decimal_places=2, max_digits=7)),
                ('mainboard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainboard.Mainboard_info')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Market_info')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='mainboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainboard.Mainboard_info'),
        ),
    ]
