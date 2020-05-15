import logging
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from BlogApp.models import BlogPost, Comments, Likes
from BlogApp.forms import EmailForm,CommentsForm
from BlogApp.exceptions.exception import ApplicationException
from django.core import mail
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

logger = logging.getLogger('blogapp-logger')
# Providing the default value for tag_slug
def dispay_blog_list(request, tag_slug=None):
    logger.info('Inpput Params - {} {}'.format(request,tag_slug))
    try:
        blog_list = BlogPost.objects.filter(status = 'PUBLISHED')
        blog_list_count = blog_list.count()
        tag_flag = False
        tag = None
        if(tag_slug):
            tag = get_object_or_404(Tag, slug = tag_slug)
            blog_list = blog_list.filter(tags__in = [tag])
            tag_flag = True

        paginator = Paginator(blog_list, 3);
        try:
            page_number = request.GET.get('page')
            blog_list = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            blog_list = paginator.get_page(1)
    except Exception as e:
        logger.error(e)
        raise ApplicationException(e)
    return render(request, 'blogapp/blog_list.html', context={'blog_list':blog_list, 'blog_list_count':blog_list_count,
                                                              'tag':tag, 'tag_flag':tag_flag})

def display_blog_details(request, year, month, day, slug):
    try:
        is_comment_saved = False
        blog_post = get_object_or_404(BlogPost, slug=slug, published_date__year=year,
                                    published_date__month=month, published_date__day=day, status='PUBLISHED')
        comments_list = blog_post.comments.filter(active = True)
        like_model_obj = blog_post.likes.first();
        like_count=dislike_count = 0
        if(like_model_obj):
            like_count = like_model_obj.likes
            dislike_count = like_model_obj.dislikes
        comment_form = CommentsForm()
        if(request.method == 'POST'):
            new_comment = CommentsForm(request.POST)
            if(new_comment.is_valid()):
                new_comment = new_comment.save(commit=False)
                new_comment.blog_post = blog_post
                new_comment.save()
                is_comment_saved = True
    except Exception as e:
        logger.error(e)
        raise ApplicationException(e)
    return render(request, "blogapp/blog_details.html", context={'post_details':blog_post, 'comment_form':comment_form,
                                                                 'comments_list':comments_list,
                                                                 'is_comment_saved':is_comment_saved,
                                                                 'like_count':like_count,
                                                                 'dislike_count':dislike_count})

def share_blog_by_email(request, blog_id):
    try:
        blog = get_object_or_404(BlogPost, id = blog_id)
        email_form = EmailForm()
        is_email_sent = False
        if(request.method == 'POST'):
            email_form = EmailForm(request.POST)
            if(email_form.is_valid()):
                email_data = email_form.cleaned_data
                mail.send_mail(blog.title,blog.body,'durga.python.videos@gmail.com',['durga.python.videos01@gmail.com'], fail_silently=False)
                is_email_sent = True
    except Exception as e:
        logger.exception(e)
        raise ApplicationException(e)
    return render(request, 'blogapp/email_share.html', context={'email_form':email_form, 'blog':blog,'is_email_sent':is_email_sent})

def like_blog(request):
    try:
        blog_id = request.GET['blog_id']
        liked_blog = get_object_or_404(BlogPost, id = blog_id)
        like_object = Likes.objects.filter(blog_post_id = blog_id).first()
        if(like_object is None):
            like_object = Likes()

        like_object.likes += 1
        print(like_object.likes)
        print(type(like_object.likes))
        like_object.blog_post = liked_blog
        like_object.save()
    except Exception as e:
        logger.exception(e)
        raise ApplicationException(e)
    return JsonResponse({'like_count':like_object.likes})

def dislike_blog(request):
    try:
        blog_id = request.GET['blog_id']
        liked_blog = get_object_or_404(BlogPost, id = blog_id)
        like_object = Likes.objects.filter(blog_post_id = blog_id).first()
        if(like_object is None):
            like_object = Likes()

        like_object.dislikes += 1
        like_object.blog_post = liked_blog
        like_object.save()
    except Exception as e:
        logger.exception(e)
        raise ApplicationException(e)
    return JsonResponse({'dislike_count':like_object.dislikes})
