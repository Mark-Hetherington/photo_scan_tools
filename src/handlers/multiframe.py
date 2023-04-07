from finder.base import Photo, Finder
from handlers.base import PhotoHandler


class MultiframeHandler(PhotoHandler):
    """ Combines multiple frames into one image """

    def process(self, photo: Photo, finder: Finder):
        for frame in photo.frames:
            target_path = frame.location.replace("_a", "_b")
            if finder.get_photo_by_location(target_path):
                finder.group_photos(photo, finder.get_photo_by_location(target_path))


