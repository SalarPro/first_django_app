from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='banners/', default='banners/default.jpg', blank=True)
    
    def __str__(self):
        return self.title