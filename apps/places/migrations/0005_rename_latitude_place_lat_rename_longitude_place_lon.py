# Generated by Django 4.1.6 on 2023-03-17 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_remove_place_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='longitude',
            new_name='lon',
        ),
    ]
