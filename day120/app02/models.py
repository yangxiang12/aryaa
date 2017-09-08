from django.db import models

# Create your models here.


class UserGroup(models.Model):
    group = models.CharField(max_length=32, verbose_name="用户组")


class tag(models.Model):
    name=models.CharField(max_length=32, verbose_name="用户名")