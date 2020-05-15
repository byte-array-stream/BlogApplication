from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    STATUS_CHOICE = [('DRAFT', 'Draft'),('PUBLISHED','Published')]

    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=256, unique_for_date='published_date')
    body = models.TextField()
    # To get the data from USER table only.
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    created_ts = models.DateTimeField(auto_now_add=True)
    last_updated_ts = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICE, default='DRAFT')
    tags = TaggableManager()

    class Meta:
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse("display_blog_details",args=[self.published_date.year, self.published_date.strftime('%m'),
            self.published_date.strftime('%d'),self.slug])

class Comments(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment = models.TextField()
    created_ts = models.DateField(auto_now_add=True)
    last_updated_ts = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_ts',)

class Likes(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='likes', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_ts = models.DateField(auto_now_add=True)
    last_updated_ts = models.DateField(auto_now=True)
