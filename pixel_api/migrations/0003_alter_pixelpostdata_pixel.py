# Generated by Django 4.0 on 2021-12-19 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_api', '0002_pixel_pixelpostdata_delete_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixelpostdata',
            name='pixel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pixel_api.pixel'),
        ),
    ]
