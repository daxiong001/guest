# Generated by Django 2.1.7 on 2019-03-03 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='reate_time',
            new_name='create_time',
        ),
    ]
