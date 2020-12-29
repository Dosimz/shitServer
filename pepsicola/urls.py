"""abstra_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls

from rest_framework_jwt.views import obtain_jwt_token
# from django.views.static import serve
# from abstra_user import settings

from blogs.views import BlogModelViewset, TagModelViewset, CommentModelViewset
from useroperate.views import UserFavorsViewset, ApiLaohuangliView, CreateImageViewset, ConstellationView, HotTrendsView
from users.views import EmailCodeViewset, UserViewset

from rest_framework import routers


from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'user/favors', UserFavorsViewset, basename='user_favors')
router.register(r'codes', EmailCodeViewset, basename="codes")
router.register(r'user', UserViewset, basename="users")
router.register(r'blogs', BlogModelViewset, basename="blogs")
router.register(r'tags', TagModelViewset, basename="tags")
router.register(r'comments', CommentModelViewset, basename="comments")
router.register(r'imagetest', CreateImageViewset, basename="imagetest")


# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    # path('user/logout/', TestView.as_view()),
    path('user/login/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    # re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('laohuangli/', ApiLaohuangliView.as_view()),
    path('constellation/', ConstellationView.as_view()),
    path('hosttrends/', HotTrendsView.as_view()),
    # path('api/v1/blog/<int:blog_id>', BlogView.as_view()),
    # path('userfavors/', UserFavorsViewset.as_view()),
    path('', include(router.urls)),
    re_path(r'^docs/', include_docs_urls(title="个人博客API文档")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
