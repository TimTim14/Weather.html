# Generated by Django 2.1.5 on 2019-04-15 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190123_2047'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Humidity',
        ),
        migrations.RenameField(
            model_name='temperature',
            old_name='recorded_at',
            new_name='recorded_at',
        ),
    ]
