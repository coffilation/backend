# Generated by Django 4.1.6 on 2023-04-13 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compilations', '0007_alter_compilation_options_compilation_members_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compilation',
            options={'default_permissions': [], 'permissions': [('compilations.change_compilation', 'Изменение данных коллекции'), ('compilation.change_places_list', 'Изменение списка точек в коллекции')]},
        ),
    ]