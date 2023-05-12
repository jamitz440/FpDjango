# Generated by Django 4.2.1 on 2023-05-12 20:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('material', models.CharField(choices=[('PLA', 'PLA'), ('ABS', 'ABS'), ('PETG', 'PETG'), ('TPU', 'TPU'), ('Nylon', 'Nylon'), ('ASA', 'ASA'), ('PC', 'PC'), ('Carbon Fibre', 'Carbon Fibre')], max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('hex', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
                ('etsy_link', models.CharField(default='https://www.etsy.com/shop/FitzPrintsgb', max_length=1000)),
                ('description', models.TextField()),
                ('print_time', models.FloatField()),
                ('weight', models.FloatField()),
                ('filament_cost', models.FloatField()),
                ('cost', models.FloatField()),
                ('profit', models.FloatField(blank=True)),
                ('colour_h', models.CharField(blank=True, max_length=100)),
                ('colour_s', models.CharField(blank=True, max_length=100)),
                ('colour_l', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])])),
                ('filament_used', models.ManyToManyField(blank=True, to='core.filament')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]