# -*- coding: UTF-8 -*-
from flask import Blueprint


class FlaskUpload(object):

    def __init__(self, app):
        self.blueprint = Blueprint("flask_upload__", __name__,
                                   static_folder="static",
                                   template_folder="templates")
        self.app = app
        self.app.register_blueprint(self.blueprint,
                                    url_prefix="/flask_upload__")
