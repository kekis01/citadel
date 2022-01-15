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
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-time_create']


class Comments(models.Model):
    article_id = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    likes = models.ManyToManyField(User, related_name='comment_post')

    def total_likes(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_tag(self):
        if self.name == 'CS:GO':
            return "cs-go"
        elif self.name == 'DOTA 2':
            return "dota-2"
        elif self.name == 'FIFA':
            return "fifa"
        elif self.name == 'League of Legends':
            return "lol"
        else:
            return "event"
