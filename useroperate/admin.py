from django.contrib import admin
from useroperate.models import favor_article
# Register your models here.

class FavorInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'articles', 'add_time')

admin.site.register(favor_article, FavorInfoAdmin)