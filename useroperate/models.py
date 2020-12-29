from django.db import models
from users.models import UserModel
from blogs.models import Article, Tag
from datetime import  datetime
# Create your models here.


class favor_article(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='用户', related_name="favors")
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="收藏的文章", related_name="favors_a", help_text='文章id')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "文章收藏记录"
        verbose_name_plural = verbose_name
        unique_together = ("user", "articles")

    def __str__(self):
        return self.user.name


class favor_taps(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='用户')
    taps = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="用户的标签")

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name
        unique_together = ("user", "taps")

    def __str__(self):
        return self.user.username