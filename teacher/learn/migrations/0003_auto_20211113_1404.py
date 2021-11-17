# Generated by Django 3.2.5 on 2021-11-13 13:04

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
