# Generated by Django 3.2.5 on 2021-11-16 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_auto_20211116_1515'),
        ('learn', '0005_alter_profile_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]
