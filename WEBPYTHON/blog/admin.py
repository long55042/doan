from django.contrib import admin

from .models import Post

from .models import avatar

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body','date',]
    list_filter = ['date']
    search_fields = ['title']
    # list_display = ['response']
admin.site.register(Post,PostAdmin)
# Register your models here.

class PostAdmin1(admin.ModelAdmin):
    list_display = ['title','date', 'image', 'author','email_page', 'phone']
    list_filter = ['date']
    search_fields = ['title']
    # list_display = ['response']
admin.site.register(avatar,PostAdmin1)

