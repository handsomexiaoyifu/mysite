from django.db import models 
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户名')

    nickname = models.CharField(max_length=20,verbose_name='昵称')

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)

    class Meta:
        ordering = ['id']
        verbose_name = '个人信息'
        verbose_name_plural = '个人信息'  # 复数形式

def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''

def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username

def has_nickname(self):
    return Profile.objects.filter(user=self).exists()

User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname