# Generated by Django 4.0 on 2021-12-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_api', '0011_user_remove_pixel_client_email_alter_pixel_client_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('grade', models.IntegerField()),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pixel',
            name='pixel_type',
            field=models.CharField(choices=[('tracking', 'Main'), ('conversion', 'Conversion')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
