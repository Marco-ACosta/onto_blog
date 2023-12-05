from django.contrib import admin
from blog.models import Post

class ListPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'posted_at']
    list_display_links = ['id', 'title', 'body', 'posted_at']
    search_fields = ['id', 'title']
    ordering = ['id', 'title', 'body', 'posted_at']
    list_per_page = 10
    readonly_fields = ['author']
    exclude = ['comments', 'likes']
    
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()




admin.site.register(Post, ListPost)
