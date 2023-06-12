from django.contrib import admin
from myblog.models import blogs_db
from myblog.models import accounts
# Register your models here.

class blogs_content(admin.ModelAdmin):
    list_display=("title","subtitle","tags")


admin.site.register(blogs_db,blogs_content)


class myacc(admin.ModelAdmin):
    list_display=("Username","Password","Email")

admin.site.register(accounts, myacc)