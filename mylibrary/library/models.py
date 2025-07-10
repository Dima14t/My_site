from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')  # статическое изображение обложки

    def __str__(self):
        return self.title