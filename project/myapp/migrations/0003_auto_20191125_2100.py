# Generated by Django 2.2.7 on 2019-11-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_plant_plantdisease_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='GrowthHabit',
            new_name='ControlMethod',
        ),
    ]
