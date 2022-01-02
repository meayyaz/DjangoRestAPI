# Generated by Django 4.0 on 2021-12-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_api', '0003_alter_pixelpostdata_pixel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixel',
            name='pixel_type',
            field=models.CharField(choices=[('main', 'Main'), ('conversion', 'Conversion')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pixelpostdata',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
