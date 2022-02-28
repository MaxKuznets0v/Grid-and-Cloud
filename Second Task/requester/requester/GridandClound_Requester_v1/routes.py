# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.request import Request
from .api.register import Register


routes = [
    dict(resource=Request, urls=['/request'], endpoint='request'),
    dict(resource=Register, urls=['/register'], endpoint='register'),
]