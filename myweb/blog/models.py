from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="博客分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = "博客分类"


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="博客标签")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = "博客标签"


class Entry(models.Model):
    title = models.CharField(max_length=128, verbose_name="文章标题")
    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name="博客配图")

    body = models.TextField(verbose_name="博客正文")

    abstract = models.TextField(max_length=256, blank=True, null=True, verbose_name='博客摘要')
    visting = models.PositiveIntegerField(default=0, verbose_name='博客访问量')