# -*- coding: UTF-8 -*-
import pkg_resources
from flask import render_template_string


class FileInput(object):

    def __call__(self, field, **kwargs):

        if not field.multiple:
            # TODO return a widget like http://jasny.github.io/bootstrap/javascript/#fileinput
            return ''
        else:
            s = pkg_resources.resource_string(__name__,
                                              'templates/uploader.html')
            return render_template_string(s, field_name=field.name)
