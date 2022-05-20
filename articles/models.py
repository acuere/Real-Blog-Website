from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150,default='')
    summary = models.CharField(max_length=500, blank=True)
    body = models.TextField(default='')
    picture = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])





