from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_new = models.DateTimeField(auto_now_add=True)
    updated_new = models.DateTimeField(auto_now=True)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
