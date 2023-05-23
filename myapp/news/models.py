from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Новая статья')
    anons = models.CharField('Анонс', max_length=50, default='Новый анонс')
    full_text = models.TextField('Статья')
    aughtor = models.CharField('Автор', max_length=20, null=True)
    date = models.DateTimeField('Дата публикации')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
