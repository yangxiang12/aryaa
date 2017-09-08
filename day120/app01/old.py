#!/usr/bin/python
# -*- coding: UTF-8 -*-
from old.service import v1
from app01 import models
from django.utils.safestring import mark_safe
from django.urls import reverse


class OldUserInfo(v1.BaseOldAdmin):

    def func(self,obj=None,is_header=None):
        if is_header:
            return '操作'
        else:
            name = "{0}:{1}_{2}_change".format(self.site.namespace,self.model_class._meta.app_label,self.model_class._meta.model_name)
            url = reverse(name,args=(obj.pk,))#获取的就是自动生成的id，根据id进行修改操作
            return mark_safe("<a href='{0}'>编辑</a>".format(url))

    def checkbox(self,obj=None,is_header=None):
        if is_header:
            return mark_safe("<input type='checkbox'/>")
        else:
            tag = "<input type='checkbox' value='{0}' />".format(obj.pk)
            return mark_safe(tag)

    list_display = [checkbox,'id','username','email',func]#tbody里面的数据

v1.site.register(models.UserInfo,OldUserInfo)




class OldRole(v1.BaseOldAdmin):

    def func(self,obj=None,is_header=None):
        if is_header:
            return '操作'
        else:
            name = "{0}:{1}_{2}_change".format(self.site.namespace,self.model_class._meta.app_label,self.model_class._meta.model_name)
            url = reverse(name,args=(obj.pk,))#获取的就是自动生成的id，根据id进行修改操作
            return mark_safe("<a href='{0}'>编辑</a>".format(url))

    def checkbox(self,obj=None,is_header=None):
        if is_header:
            return mark_safe("<input type='checkbox'/>")
        else:
            tag = "<input type='checkbox' value='{0}' />".format(obj.pk)
            return mark_safe(tag)

    list_display = [checkbox,'id','name',func]

v1.site.register(models.Role,OldRole)



