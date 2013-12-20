# -*- coding: UTF-8 -*-
from wtforms import fields
from werkzeug import FileStorage
from .widgets import FileInput


# TODO provides more validators
class FileField(fields.Field):

    widget = FileInput()
    type = 'FileField'

    def __init__(self, label='', validators=None, save_path=None, max_num=1,
                 preview_size=(128, 128),
                 *args, **kwargs):
        super(FileField, self).__init__(label, validators, *args, **kwargs)
        self.save_path = save_path
        self.max_num = max_num
        self.preview_size = preview_size

    @property
    def multiple(self):
        return self.max_num > 1

    def has_file(self):
        '''Return True iff self.data is a FileStorage with file data'''
        if not self.data:
            return False
        if not all(isinstance(fs, FileStorage) for fs in self.data):
            return False
        # filename == None => the field was present but no file was entered
        # filename == '<fdopen>' is for a werkzeug hack:
        #   large file uploads will get stored in a temporary file on disk and
        #   show up as an extra FileStorage with name '<fdopen>'
        return any(fs.filename not in [None, '', '<fdopen>'] for fs in
                   self.data)

    def process_formdata(self, valuelist):
        self.data = valuelist
