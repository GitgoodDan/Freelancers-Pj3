# Generated by Django 5.0.3 on 2024-03-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_freelancerprofile_delivery_freelancerprofile_located'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freelancerprofile',
            old_name='delivery',
            new_name='delivery_time',
        ),
        migrations.AlterField(
            model_name='freelancerprofile',
            name='located',
            field=models.CharField(choices=[('us_only', 'US Only'), ('worldwide', 'Worldwide')], max_length=20),
        ),
    ]