from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']