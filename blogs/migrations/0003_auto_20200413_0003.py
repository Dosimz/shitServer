# Generated by Django 3.0.3 on 2020-04-12 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_auto_20200409_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '博客文章', 'verbose_name_plural': '博客文章'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': '用户评论'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '文章标签管理', 'verbose_name_plural': '文章标签管理'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myarticles', to=settings.AUTH_USER_MODEL, verbose_name='作者名称'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(help_text='文章内容', verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='文章标题', max_length=44, verbose_name='文章题目'),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, help_text='文章阅读量，默认为0', verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(help_text='文章id', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.Article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(help_text='评论内容', max_length=200, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='标签名', max_length=20, unique=True, verbose_name='文章标签'),
        ),
    ]