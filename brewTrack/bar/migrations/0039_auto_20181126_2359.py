# Generated by Django 2.1.2 on 2018-11-27 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0038_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
