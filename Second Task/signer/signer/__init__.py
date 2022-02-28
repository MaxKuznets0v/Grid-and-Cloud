# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import GridandClound_Signer_v1
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    db = SQLAlchemy(app)

    class Users(db.Model):
        id = db.Column(db.String(40), primary_key=True)
        email = db.Column(db.String(100))
        password = db.Column(db.String(100))

    db.create_all()

    app.register_blueprint(
        GridandClound_Signer_v1.bp,
        url_prefix='')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)