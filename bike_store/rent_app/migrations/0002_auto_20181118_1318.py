# Generated by Django 2.1.3 on 2018-11-18 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adress',
            new_name='address',
        ),
    ]
