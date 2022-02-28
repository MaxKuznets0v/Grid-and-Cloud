# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import uuid
import xml.etree.ElementTree as ET
from . import utils

from . import Resource
from .. import schemas
import sqlite3


class User(Resource):

    def post(self):
        raw_data = ET.fromstring(request.get_data())
        email = raw_data.find('email').text
        password = raw_data.find('password').text
        id = str(uuid.uuid4())

        conn = sqlite3.connect('users.sqlite3')
        cur = conn.cursor()

        cur.execute(f'SELECT id FROM users WHERE users.email = "{email}"')
        res = cur.fetchall()

        if len(res) > 0:
            return utils.resp_xml("USER ALREADY EXISTS", 400)
        cur.execute(f'INSERT INTO users (id, email, password) VALUES ("{id}", "{email}", "{password}")')
        conn.commit()

        cur.execute('SELECT * FROM users')
        res = cur.fetchall()
        print(res)
        return utils.resp_xml("USER CREATED", 201)