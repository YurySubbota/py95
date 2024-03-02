from django.contrib import admin
from blog.models import Post


# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title',)


admin.site.register(Post, PostModelAdmin)
