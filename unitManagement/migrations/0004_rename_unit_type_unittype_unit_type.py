# Generated by Django 4.0.3 on 2022-03-26 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unitManagement', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unittype',
            old_name='unit_Type',
            new_name='unit_type',
        ),
    ]