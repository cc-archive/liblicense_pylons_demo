import os
from pylons import config

import liblicense

class Photo(object):

    def __init__(self, id, location):
        self.id = id
        self.location = location

        self.title = '(untitled)'
        self.license = None

    def __str__(self):
        return self.title

    @property
    def license_name(self):
        if self.license == None:
            return '(unlicensed)'

        return liblicense.get_name(self.license)

    @property
    def thumbnail_location(self):

        return '%s.thumb%s' % os.path.splitext(self.location)
