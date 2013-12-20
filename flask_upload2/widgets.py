# -*- coding: UTF-8 -*-
import pkg_resources
from flask import render_template


class FileInput(object):

    def __call__(self, field, **kwargs):
        # TODO no image no preview
        return render_template('flask_upload2__/uploader.html',
                                field_name=field.name,
                                max_num=field.max_num,
                                preview_size=field.preview_size)
