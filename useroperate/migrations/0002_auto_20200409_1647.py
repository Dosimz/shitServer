# Generated by Django 3.0.3 on 2020-04-09 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useroperate', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_auto_20200409_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='favor_taps',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='favor_article',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favors_a', to='blogs.Article', verbose_name='收藏的文章'),
        ),
        migrations.AddField(
            model_name='favor_article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favors', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='favor_taps',
            unique_together={('user', 'taps')},
        ),
        migrations.AlterUniqueTogether(
            name='favor_article',
            unique_together={('user', 'articles')},
        ),
    ]
