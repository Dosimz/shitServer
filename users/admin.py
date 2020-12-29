from django.contrib import admin
from users.models import UserModel, VerifyCode
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email', 'date_joined', 'user_state')
    # list_display = ['id', 'title', 'get_tags', 'author_name', 'views', 'created_time', 'modified_time']
    # def get_tags(self, obj):
    #     return "\n".join([t.name for t in obj.tags.all()])

    list_per_page = 50
    list_display_links = ('id', 'name')

    search_fields = ['name', 'email']
    list_filter = ['user_state']
    date_hierarchy = 'date_joined'

admin.site.register(UserModel, UserInfoAdmin)