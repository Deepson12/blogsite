from django.contrib import admin
from myblog.models import blogs_db
# Register your models here.

class blogs_content(admin.ModelAdmin):
    list_display=("title","subtitle","tags")


admin.site.register(blogs_db,blogs_content)
