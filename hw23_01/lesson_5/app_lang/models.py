
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='book name')


    published_at = models.DateField(verbose_name='published at')
    description = models.TextField(verbose_name='description')

    class Meta:

        verbose_name = 'book'
        verbose_name_plural = 'books'

        def __str__(self):
            return f'{self.name}'

