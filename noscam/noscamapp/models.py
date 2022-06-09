from django.db import models


class Scamer(models.Model):
    name = models.CharField(max_length=20, verbose_name='Никнейм')
    money = models.IntegerField(verbose_name='Зелень')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время регестрации')

    class Meta:
        verbose_name = 'Скамеры'
        verbose_name_plural = 'Скамеры'
        ordering = ['pk', 'name']


class Scam(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    totalScams = models.IntegerField()
    scamer = models.ForeignKey('Scamer', on_delete=models.CASCADE)