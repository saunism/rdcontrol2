from django.db import models

class Article(models.Model):
    article_name = models.CharField('Название статьи',max_length=100)
    article_discription = models.CharField('Краткое описание статьи',max_length=250)
    article_text = models.TextField('Текст статьи')
    article_pub_date = models.DateTimeField('Время публикации статьи')
    article_author = models.CharField('Автор',max_length=50)
    article_category = models.CharField('Категория',max_length=50,default="other")
    was_checked_by_admin = models.BooleanField("Можно публиковать",default=False)
    