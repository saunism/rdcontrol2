# Generated by Django 3.0.3 on 2020-04-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ani_helper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='was_checked_by_admin',
            field=models.BooleanField(default=False, verbose_name='Можно публиковать'),
        ),
    ]
