# Generated by Django 3.2.18 on 2023-05-16 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0014_add_missing_fields_to_django_scheme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthfacilitycatchment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='healthfacilitylegalform',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='healthfacilitysublevel',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='officervillage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='userdistrict',
            options={'managed': True},
        ),
    ]