from django.contrib import admin
from .models import Article, Tag, Comment
from useroperate.models import favor_article
# Register your models here.

class ComentInline(admin.TabularInline):
    model = Comment

class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_tags', 'author', 'views', 'created_time', 'modified_time')
    # list_display = ['id', 'title', 'get_tags', 'author_name', 'views', 'created_time', 'modified_time']
    def get_tags(self, obj):
        return "\n".join([t.name for t in obj.tags.all()])

    list_per_page = 50
    list_display_links = ('id', 'title')

    search_fields = ['title']
    list_filter = ['author']
    date_hierarchy = 'created_time'
    # list_editable = ['title']
    inlines = [ComentInline]
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('title', 'body', 'author', 'views',)
    #     }],
        # ['Advance', {
        #     'classes': ('collapse',),
        #     'fields': ('',)
        # }]
    # )
    # fk_fields = ['author']

class CommentInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'reviewer', 'created_time')


admin.site.register(Tag)
admin.site.register(Article, ArticleTagAdmin)
admin.site.register(Comment, CommentInfoAdmin)
admin.site.site_header = '博客后台管理系统'
admin.site.site_title = '博客后台管理系统'

# admin.site.register(Tag)
# admin.site.register(Article)