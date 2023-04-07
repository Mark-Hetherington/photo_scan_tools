from finder.base import Photo, Finder
from handlers.base import PhotoHandler


class AnnotationHandler(PhotoHandler):
    """ Tries to detect an image which is annotated, and convert that to a title """

    def process(self, photo: Photo, finder: Finder):
        pass

