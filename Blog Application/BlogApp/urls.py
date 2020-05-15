from django.urls import path, re_path
from BlogApp import views

urlpatterns = [
    path('likepost/', views.like_blog),
    path('dislikepost/', views.dislike_blog),
    path('blog_list/', views.dispay_blog_list, name = 'blog_list'),
    re_path('^blog_list/(?P<tag_slug>[-\w]+)/$', views.dispay_blog_list, name = 'blog_list_diplay'),
    re_path('^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.display_blog_details, name = 'display_blog_details'),
    re_path('^share_blog/(?P<blog_id>[-\w]+)/$', views.share_blog_by_email)
]
