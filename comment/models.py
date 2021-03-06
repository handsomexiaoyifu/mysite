from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()
    
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='评论内容')

    comment_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')

    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE,verbose_name='发布人')

    root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.CASCADE,verbose_name='评论对象')

    parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.CASCADE)

    reply_to = models.ForeignKey(User, related_name="replies", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_url(self):
        return self.content_object.get_url()

    def get_user(self):
        return self.user

    class Meta:
        ordering = ['-comment_time']
        verbose_name = '评论'
        verbose_name_plural = '评论'  # 复数形式