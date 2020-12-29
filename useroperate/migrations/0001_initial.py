# Generated by Django 3.0.3 on 2020-04-09 08:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favor_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户喜欢的文',
                'verbose_name_plural': '用户喜欢的文',
            },
        ),
        migrations.CreateModel(
            name='favor_taps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Tag', verbose_name='用户的标签')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
    ]
