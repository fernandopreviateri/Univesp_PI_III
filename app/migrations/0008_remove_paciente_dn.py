# Generated by Django 2.2.1 on 2021-11-10 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211110_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='dn',
        ),
    ]
