# Generated by Django 3.0.3 on 2020-04-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ani_helper', '0002_article_was_checked_by_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_pub_date',
            field=models.DateTimeField(verbose_name='Время публикации статьи'),
        ),
    ]
