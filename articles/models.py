from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150,default='')
    summary = models.CharField(max_length=500, blank=True)
    body = RichTextField()
    picture = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)




