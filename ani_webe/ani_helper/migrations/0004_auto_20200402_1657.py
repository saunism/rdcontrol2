# Generated by Django 3.0.3 on 2020-04-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ani_helper', '0003_auto_20200401_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.CharField(default='other', max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
    ]
