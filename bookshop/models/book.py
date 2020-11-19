from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/files', max_length=100)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails')
    link = models.CharField(null=True, max_length=50)
    fileSize = models.CharField(null=True)


class BookImages(models.Model):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/image', blank=True)
