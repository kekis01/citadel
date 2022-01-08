from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    source = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Comments(models.Model):
    article_id = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    like_count = models.IntegerField(default=0)
    liked_by_user = models.BooleanField(default=False)