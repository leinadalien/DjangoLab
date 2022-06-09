from django.db import models


class Scamer(models.Model):
    name = models.CharField(max_length=20)
    money = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
