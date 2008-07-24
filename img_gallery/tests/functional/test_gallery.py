from img_gallery.tests import *

class TestGalleryController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='gallery'))
        # Test response...
