# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, Response
import requests

from . import Resource
from .. import schemas


class Request(Resource):

    def post(self):
        data = request.get_data()
        res = requests.post('http://127.0.0.1:5000/document', data)
        r = Response(response=res.content, status=res.status_code, mimetype="application/xml")
        r.headers["Content-Type"] = "text/xml; charset=utf-8"
        return r