import json

from rest_framework import serializers
from .models import Article, Tag, Comment
from users.models import UserModel
from useroperate.models import favor_article


class BlogModelSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=UserModel.objects.all(),
        default=serializers.CurrentUserDefault(), help_text='作者(该参数默认使用当前登录用户)'
    )

    like_num = serializers.SerializerMethodField()
    def get_like_num(self, row):
        # ret = str(row.favors_a.all())
        ret = len(row.favors_a.all())
        return ret

    review_num = serializers.SerializerMethodField()
    def get_review_num(self, row):
        # ret = str(row.favors_a.all())
        ret = len(row.comments.all())
        return ret

    class Meta:
        model = Article
        fields = ("id", "title", "author", "tags", "body", "like_num", "views", "review_num", "modified_time")
        depth = 1

    def create(self, validated_data):
        obj_tags = []
        for i in self.context["request"].data.get('tags'):
            print(i)
            tag_obj = Tag.objects.get(name=i)
            obj_tags.append(tag_obj)
        # set_tags = set(obj_tags)
        # print(type(set_tags))
        article = Article.objects.create(**validated_data)
        # instance = Setupuser.objects.create(organization=org)
        # instance.emails_for_help.set(users)
        article.tags.set(obj_tags)
        return article


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "id")

class CommentModelSerializer(serializers.ModelSerializer):
    # reviewer = serializers.SlugRelatedField(slug_field="name", queryset=UserModel.objects.all(),
    #     default=serializers.CurrentUserDefault()
    # )
    reviewer = serializers.SerializerMethodField(default=serializers.CurrentUserDefault(), help_text='评论者(该参数默认使用当前登录用户)')

    class Meta:
        model = Comment
        # fields = "__all__"
        # depth = 2
        fields = ("reviewer", "content", "created_time", "article")

    def get_reviewer(self, row):
        # s = self.context["request"].GET["blogId"]
        # print(row)
        value_dict = {"name": row.reviewer.name, "avatar": str(row.reviewer.avatar), 'email': row.reviewer.email}
        return value_dict

    def create(self, validated_data):
        if 'reviewer' not in validated_data:
            validated_data['reviewer'] = self.context['request'].user
        return Comment.objects.create(**validated_data)