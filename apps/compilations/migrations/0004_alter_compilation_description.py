# Generated by Django 4.1.6 on 2023-03-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilations', '0003_remove_compilation_gradient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compilation',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]