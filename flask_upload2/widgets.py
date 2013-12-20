# -*- coding: UTF-8 -*-
import pkg_resources
from flask import render_template


class FileInput(object):

    def __call__(self, field, **kwargs):

        if not field.multiple:
            # TODO return a widget like http://jasny.github.io/bootstrap/javascript/#fileinput
            return ''
        else:
            return render_template('flask_upload2__/uploader.html',
                                   field_name=field.name,
                                   max_num=field.max_num,
                                   preview_size=field.preview_size)
