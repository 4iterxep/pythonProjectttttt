from django.core.files import images
from django.db import models




# Create your models here.
class Kuponi(models.Model):
    title = models.CharField('Магазин', max_length=50)
    description = models.CharField('Описание', max_length=250)
    code = models.CharField('Бонусный код/слово', max_length=250)
    date_exists = models.DateField('До какой даты действует')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'