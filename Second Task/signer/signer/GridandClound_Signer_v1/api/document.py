# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from . import utils
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring

from . import Resource
from .. import schemas
import sqlite3
import hashlib


class Document(Resource):

    def post(self):
        raw_data = request.get_data().decode("utf-8") 
        xml_data = ET.fromstring(request.get_data())
        email = xml_data.find('email').text
        password = xml_data.find('password').text
        
        conn = sqlite3.connect('users.sqlite3')
        cur = conn.cursor()

        cur.execute(f"SELECT id FROM users WHERE users.email = '{email}' AND users.password = '{password}'")
        res = cur.fetchall()
        if len(res) < 1:
            return utils.resp_xml("WRONG CREDENTIALS", 404)

        id = res[0][0]
        data = raw_data + id
        hsh = hashlib.sha256(data.encode()).hexdigest()
        sign = ET.Element("sign")
        sign.text = hsh
        result = ET.Element("doc")
        doc = xml_data.find('doc')
        for elem in doc:
            result.append(elem)
        result.append(sign)

        return utils.resp_xml(tostring(result), 200)