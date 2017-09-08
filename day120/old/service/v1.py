#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse,render
from django.conf.urls import url, include
from django.urls import reverse

class BaseOldAdmin(object):
    list_display = "__all__"

    def __init__(self,model_class,site):
        self.model_class = model_class
        self.site = site
        self.request = None

        self.app_label = model_class._meta.app_label
        self.model_name = model_class._meta.model_name


    @property
    def urls(self):
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        urlpatterns = [
            url(r'^$',self.changelist_view,name='%s_%s_changlist'%info),
            url(r'^add/$',self.add_view,name='%s_%s_add'%info),#http://127.0.0.1:8000/old/app01/role/add/
            url(r'^(.+)/delete/$',self.delete_view,name='%s_%s_delete'%info),#http://127.0.0.1:8000/old/app01/role/111/delete/
            url(r'^(.+)/change/$',self.change_view,name='%s_%s_change'%info)#http://127.0.0.1:8000/old/app01/role/111/change/
        ]

        return urlpatterns

    def changelist_view(self,request):
        '''
        查看列表
        :param request:
        :return:
        '''
        self.request = request
        result_list = self.model_class.objects.all()
        # print(self.model_class)#model_class :是当前的类名，小写，

        #生成页面上：添加按钮
        from django.http.request import QueryDict
        param_dict = QueryDict(mutable=True)
        if request.GET:
            param_dict['_changelistfilter'] = request.GET.urlencode()

        base_add_url = reverse("{2}:{0}_{1}_add".format(self.app_label,self.model_name,self.site.namespace))
        add_url = "{0}?{1}".format(base_add_url,param_dict.urlencode())

        context = {
            'result_list':result_list,#queryset 对象
            'list_display':self.list_display,#列表，
            'oldadmin_obj':self,#当前对象
            'add_url':add_url
        }
        return render(request,'t1/change_list.html',context)

    def add_view(self,request):
        '''
        添加数据
        :param request:
        :return:
        '''
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        data = "%s_%s_add"% info
        return HttpResponse(data)

    def delete_view(self,request,pk):
        '''
        删除
        :param request:
        :return:
        '''
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        data = "%s_%s_del"% info
        return HttpResponse(data)

    def change_view(self,request,pk):
        '''
        查看
        :param request:
        :return:
        '''
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        data = "%s_%s_change"% info
        return HttpResponse(data)


class OldSite(object):
    def __init__(self):
        self._registry = {}
        self.namespace = 'old'
        self.app_name = 'old'

    def register(self,model_class,xxx = BaseOldAdmin):
        self._registry[model_class] = xxx(model_class,self)#实例化出一个BaseOldAdmin对象，‘model_class’

    def get_url(self):
        ret = []
        for model_cls,old_admin_obj in self._registry.items():#遍历self._registry = {}，字典里面都是BaseOldAdmin实例化后的对象。
            # print('------======',old_admin_obj.urls)
            app_label = model_cls._meta.app_label#获取app名称
            model_name = model_cls._meta.model_name#获取model名称
            print(model_cls,app_label,model_name)
            ret.append(url(r'^%s/%s/'%(app_label,model_name),include(old_admin_obj.urls)))#urls是BaseOldAdmin的urls方法
        return ret

    @property
    def urls(self):
        #self.get_url():返回的结果是:
            #[ url(r'app01/userinfo/', include()),
            #   url(r'^logout/', self.logout,name='logout'),]
        return self.get_url(),self.app_name,self.namespace

    def login(self,request):
        return HttpResponse('login')

    def logout(self,request):
        return HttpResponse('logout')


site = OldSite()