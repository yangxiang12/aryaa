#!/usr/bin/python
# -*- coding: UTF-8 -*-

from old.service import v1
from app02 import models

v1.site.register(models.UserGroup)
v1.site.register(models.tag)