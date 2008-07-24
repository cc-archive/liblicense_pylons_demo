import logging

from pylons import config

from img_gallery.lib.base import *

log = logging.getLogger(__name__)

class GalleryController(BaseController):

    def index(self):

        c.photos = model.Session.query(model.Photo).all()

        return render('/gallery-index.mako')
