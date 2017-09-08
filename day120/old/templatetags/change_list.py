#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.template import Library
from types import FunctionType

register = Library()

def inner(result_list,list_display,oldadmin_obj,):
    for row in result_list:
        if list_display == '__all__':
            yield [str(row)]
        else:
            # yield [getattr(row,name) for name in list_display]
            yield [ name(oldadmin_obj,row) if isinstance(name,FunctionType) else getattr(row,name) for name in list_display]

def table_head(list_display,oldadmin_obj):
    if list_display == '__all__':
        yield '对象列表'
    else:
        for item in list_display:
            if isinstance(item,FunctionType):
                yield item(oldadmin_obj,is_header=True)


            else:
                  yield oldadmin_obj.model_class._meta.get_field(item).verbose_name



@register.inclusion_tag('t1/md.html')
def func(result_list,list_display,oldadmin_obj):
    v = inner(result_list,list_display,oldadmin_obj)

    h = table_head(list_display,oldadmin_obj)

    return {"xx":v,'t_list':h}

