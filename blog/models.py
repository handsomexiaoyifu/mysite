from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail


class BlogType(models.Model):
    type_name = models.CharField(max_length=64,verbose_name='博客分类')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'#复数形式
        

class Blog(models.Model, ReadNumExpandMethod):

    title = models.CharField(max_length=128,verbose_name='文章标题')

    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING,verbose_name='博客分类')

    content = RichTextUploadingField(verbose_name='正文')

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='博客作者')

    read_details = GenericRelation(ReadDetail)

    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    last_updated_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_user(self):
        return self.author

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>" % self.title


    class Meta:
        ordering = ['-created_time']#按字段排序 防止报错
        verbose_name = '博客'
        verbose_name_plural = '博客'  # 复数形式