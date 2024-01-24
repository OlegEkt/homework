from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(verbose_name='birthdate')
    tel = models.CharField(max_length=16)
    news_num = models.IntegerField(default=0, verbose_name='кол-во публикаций')

    def __str__(self):
        return f'{self.user.email}'

class Record(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='профиль')
    title = models.CharField(max_length=256, verbose_name='заголовок')
    description = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    class Meta:
        db_table = 'records'
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ['-created_at']

