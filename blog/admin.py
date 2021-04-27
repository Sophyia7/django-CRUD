from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline): 
  model = Comment
  extra = 0

class PostAdmin(admin.ModelAdmin): 
  inlines = [ CommentInline, ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment) 

