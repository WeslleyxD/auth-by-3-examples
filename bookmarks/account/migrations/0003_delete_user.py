# Generated by Django 4.0.6 on 2022-07-14 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]