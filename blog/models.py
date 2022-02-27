from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-date_posted',)
    title = models.CharField(max_length=100)
    post_description = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    post_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
