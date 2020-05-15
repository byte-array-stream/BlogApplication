from django import template
from math import ceil
from django.db.models import Count
from BlogApp.models import BlogPost

register = template.Library()

#Simple tag - returns a string after processing
@register.simple_tag(name='total_post_count')
def total_posts():
    return BlogPost.objects.filter(status ='PUBLISHED').count()

# inclusion tag - Returns a rendered HTML with data
# This method returns latest 5 blogs and top 5 highest commented blogs
@register.inclusion_tag('blogapp/latest_blogs.html')
def latest_blog_posts():
    latest_blogs = BlogPost.objects.filter(status ='PUBLISHED').order_by('-created_ts')[0:5]
    hieghest_commented_blogs = BlogPost.objects.defer('body').annotate(comment_count = Count('comments')).order_by('-comment_count')[0:5]
    return {'latest_blogs':latest_blogs,'hieghest_commented_blogs':hieghest_commented_blogs}
