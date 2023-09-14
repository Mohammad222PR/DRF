from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/article', blank=True, null=True)
    body = models.TextField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=1000000000)
    created = models.DateField()

    def __str__(self):
        return self.text
