from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

# def define_name():
#     datetime.now().strftime('%Y%m%d%H%M%S%f')

class UserModel(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    email = models.CharField('e-mail', max_length=24, unique=True)
    phone_num = models.CharField('phone number', max_length=11, unique=False)
    name = models.CharField(max_length=20, null=False, blank=True, default=datetime.now().strftime('%Y%m%d%H%M%S%f'), verbose_name="昵称", help_text='昵称')
    avatar = models.ImageField(upload_to='avatars/', default="avatars/default_avatar.png", verbose_name="头像", help_text='用户头像')
    birth_date = models.DateTimeField(null=True, help_text='出生日期')
    user_dsc = models.TextField(max_length=100, null=True, help_text='个人描述')
    user_state = models.CharField(max_length=4, null=True, help_text='用户状态')


    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name+'('+self.username+')'


class VerifyCode(models.Model):
    """
    邮件验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    email = models.CharField(max_length=24, verbose_name="邮箱")
    # add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    print(datetime.now())

    class Meta:
        verbose_name = "邮件验证码管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code