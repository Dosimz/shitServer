from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework import serializers
from rest_framework.response import Response
from blogs import models
from .serializers import BlogModelSerializer, TagModelSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class ModelBlogSerializer(serializers.ModelSerializer):
#     # tags = serializers.StringRelatedField(source='tab_article', many=True)
#
#     class Meta:
#         model = models.Article
#         # fields = "__all__"
#         fields = ('id', 'title', 'body',  'image', 'views', 'favor_num', 'modified_time',  'author', 'tags')
#         depth = 1

# class BlogView(APIView):
#
#     # authentication_classes = [JSONWebTokenAuthentication, BasicAuthentication]
#     permission_classes = []
#
#     def get(self, request, blog_id=''):
#         # print(request.get_full_path())
#         # print(request.path)
#         if blog_id:
#             data_list = models.Article.objects.get(id=blog_id)
#             ser = ModelBlogSerializer(instance=data_list, many=False)
#         else:
#             data_list = models.Article.objects.all()
#             ser = ModelBlogSerializer(instance=data_list, many=True)
#         return Response(ser.data)

class BlogModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
    查看某一篇博客文章。

    list:
    查看所有博客文章

    create:
    新建一篇博客文章

    update:
    更新文章

    partial_update:
    局部更新文章

    delete:
    删除一篇文章
    """
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_permissions(self):
        if self.action == "retrieve":
            return []
        elif self.action == "create":
            return [permissions.IsAuthenticated()]

        return []

    def retrieve(self, request, *args, **kwargs):
        print(request.path[7: 9])
        # count = 0
        blog_id = request.path[7: 8]
        data_model_article = models.Article.objects.get(id=blog_id)
        data_model_article.views += 1
        data_model_article.save()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    serializer_class = BlogModelSerializer
    queryset = models.Article.objects.all()


class TagModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
    查看某一个标签。

    list:
    查看所有标签

    create:
    新建一个标签

    update:
    更新标签

    partial_update:
    局部更新标签

    delete:
    删除一篇标签
    """
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == "retrieve":
            return []
        elif self.action == "create":
            return [permissions.IsAuthenticated()]

        return []
    serializer_class = TagModelSerializer
    queryset = models.Tag.objects.all()


# class CommentModelViewset(viewsets.ModelViewSet):
#     """
#     retrieve:
#     查看某一条评论。

#     list:
#     查看所有评论

#     create:
#     新增一条评论

#     update:
#     更新评论

#     partial_update:
#     局部更新评论

#     delete:
#     删除一条评论
#     """
#     # permission_classes = (IsAuthenticated,)
#     authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

#     def get_permissions(self):
#         if self.action == "retrieve":
#             return []
#         elif self.action == "create":
#             return [permissions.IsAuthenticated()]

#         return []
#     serializer_class = CommentModelSerializer
#     queryset = models.Comment.objects.all()