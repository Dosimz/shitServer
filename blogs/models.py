from django.db import models

# Create your models here.
from django.db import models
from users.models import UserModel

from datetime import datetime
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="文章标签", unique=True, help_text='标签名')
    # articles = models.ManyToManyField(Article, verbose_name="文章", blank=True, related_name='tab_article')

    class Meta:
        verbose_name = "文章标签管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=44, verbose_name="文章题目", help_text='文章标题')
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True, related_name='tag_article')
    # taps = models.CharField(max_length=20, verbose_name="文章标签")
    body = models.TextField(verbose_name="文章内容", help_text='文章内容')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="作者名称", related_name='myarticles')
    image = models.ImageField(upload_to='article/', verbose_name="文章图片", blank=True, null=True)
    views = models.PositiveIntegerField(verbose_name='阅读量', default=0, help_text='文章阅读量，默认为0')
    # favor_num = models.IntegerField(default=0, verbose_name="收藏数")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    # review = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="评论", default='暂时没有人评论')


    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", help_text='文章id')
    content = models.TextField(max_length=200, verbose_name="评论内容", help_text='评论内容')
    reviewer = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="评论者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    class Meta:
        verbose_name = "用户评论"
        ordering = ['-created_time']

    def __str__(self):
        return "评论 by {0} on 文章<<{1}>>".format(self.reviewer.name, self.article)