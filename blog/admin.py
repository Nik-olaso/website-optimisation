from django.contrib import admin
from blog.models import Post, Tag, Comment


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'text',
        'slug',
        'image',
        'published_at',
        'author',
        'likes',
        'tags',
    ]

    raw_id_fields = ['author', 'likes', 'tags']


class CommentAdmin(admin.ModelAdmin):

    list_display = [
        'post',
        'author',
        'text',
        'published_at',
    ]

    raw_id_fields = ['post', 'author']