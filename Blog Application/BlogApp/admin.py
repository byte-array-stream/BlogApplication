from django.contrib import admin
from BlogApp.models import BlogPost
from BlogApp.models import Comments

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    # List of coulumns to display at Admin console
    list_display=['id','title','author','body','slug','published_date','created_ts','last_updated_ts','status','tags']

    # Slug value will ppoulate automatically based on Title and body field
    prepopulated_fields={'slug':('title','body')}

    #Exclude will remove this field from the form.
    #exclude = ('author',)

    # This will make body field editable in the row itself. We no need to open the form and update.
    list_editable = ['body','title','tags']
    #To display filters
    list_filter = ('title','status')
    # While searching Django will look into this field
    search_fields = ('title','body')
    ordering = ('status','published_date')

class CommentsAdmin(admin.ModelAdmin):
    list_display=['id','name','email','comment','created_ts','last_updated_ts','active','blog_post_id']
    # This will make body field editable in the row itself. We no need to open the form and update.
    list_editable = ['name','email','comment','active']
    # While searching Django will look into this field
    search_fields = ('comment','name')
    ordering = ('active',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comments, CommentsAdmin)
