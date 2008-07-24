import os
import shutil
import tempfile
import logging

from PIL import Image
import liblicense

from img_gallery.lib.base import *

log = logging.getLogger(__name__)

class PhotoController(BaseController):

    def add(self):

        return render('/photo-add.mako')

    def edit(self, id):

        c.photo = model.Session.query(model.Photo).filter_by(id=id)[0]

        return render('/photo-edit-metadata.mako')

    def save_edits(self, id):
        photo = model.Session.query(model.Photo).filter_by(id=id)[0]

        print request.params.keys()
        photo.title = request.params['title']
        photo.license = request.params['cc_js_result_uri']
        
        model.Session.save_or_update(photo)
        model.Session.commit()

        redirect_to(h.url_for(controller='gallery', action='index'))

    def _make_unique_fn(self, upload_dir, image_fn):
        base, extension = os.path.splitext(image_fn)
        count = 0
        unique_name = os.path.join(upload_dir, 
                                   base + "_" + str(count) + extension)

        while os.path.exists(unique_name):
            count += 1
            unique_name = os.path.join(upload_dir, 
                                       base + "_" + str(count) + extension)

        return unique_name

    def _make_thumbnail(self, photo):

        MAX_WIDTH=512.0

        im = Image.open(photo.location)
        new_size = size = im.size

        if size[0] > MAX_WIDTH:
            new_size = (int(MAX_WIDTH), int(size[1]*(MAX_WIDTH / size[0])))
            print new_size

        im.thumbnail(new_size, Image.ANTIALIAS)
        im.save(photo.thumbnail_location)

    def upload(self):
        """Form upload handler."""

        # get the upload location from the configuration
        upload_dir = config.get('img_gallery.upload_location')

        # calculate the location of the uploaded file
        # WARNING: this is NOT SAFE! it does not verify the path is in
        #  the upload_dir
        upload_fn = self._make_unique_fn(upload_dir, 
                                         request.POST['new_image'].filename)

        # save the upload
        file(upload_fn, 'wb').write(request.POST['new_image'].value)

        # add the photo to the database
        photo = model.Photo(request.POST['new_image'].filename,
                            upload_fn)
        photo.title = request.params['title']

        # !!! liblicense magic
        photo.license = liblicense.read(photo.location)
        photo.title = liblicense.read(photo.location, liblicense.LL_NAME) or \
            request.POST['new_image'].filename

        # make the thumbnail
        self._make_thumbnail(photo)

        model.Session.save_or_update(photo)
        model.Session.commit()

        redirect_to(h.url_for(controller='gallery', action='index'))

    def static(self, id):
        """Return the actual image."""

        photo = model.Session.query(model.Photo).filter_by(id=id)[0]
        response.headers['Content-type'] = "image/jpeg"

        return file(photo.location, 'r').read()

    def thumbnail(self, id):
        """Return the actual image."""

        photo = model.Session.query(model.Photo).filter_by(id=id)[0]
        response.headers['Content-type'] = "image/jpeg"

        return file(photo.thumbnail_location, 'r').read()

    def stamped(self, id):
        """Return a copy of the image with embedded metadata."""

        photo = model.Session.query(model.Photo).filter_by(id=id)[0]

        # get a temp file name
        temp_fn = os.path.join(
            tempfile.gettempdir(), os.path.split(photo.location)[1])

        # copy the image
        shutil.copyfile(photo.location, temp_fn)

        # add the metadata
        liblicense.write(temp_fn, 
                         "http://purl.org/dc/elements/1.1/title", 
                         photo.title
                         )
        liblicense.write(temp_fn, liblicense.LL_LICENSE,
                         photo.license)

        # serve the file up
        response.headers['Content-type'] = "image/jpeg"
        return file(temp_fn, 'r').read()
