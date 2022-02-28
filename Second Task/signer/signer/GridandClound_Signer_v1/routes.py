# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.user import User
from .api.document import Document


routes = [
    dict(resource=User, urls=['/user'], endpoint='user'),
    dict(resource=Document, urls=['/document'], endpoint='document'),
]