from django.db import models
from django.core.exceptions import ValidationError


class Book(models.Model):
    """Model for the book class

    Args:
        models (model base class): from django model base class
    """
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/files', null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='uploads/thumbnails', null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    fileSize = models.CharField(max_length=50, null=True, blank=True)

    # Using clean to set file or link field mandatory
    def clean(self):
        """To validate the model add field in admin

        Raises:
            ValidationError: One of link or file is needed
        """
        super(Book, self).clean()
        if not self.file and self.link is None:
            raise ValidationError(
                'At least one field is needed link or file')

    def __str__(self):
        return self.name


class BookImages(models.Model):
    """Model to store book images

    """
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/image', blank=True)
