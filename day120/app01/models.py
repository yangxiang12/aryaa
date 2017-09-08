from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name="用户名")

class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    email = models.CharField(max_length=32, verbose_name="邮箱")

