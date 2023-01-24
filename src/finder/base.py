from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Frame:
    location: str


@dataclass
class Photo:
    frames: List[Frame]
    metadata_location: str

    def location(self):
        if self.frames:
            return self.frames[0].location

    title: str
    processed: bool = False


class Finder(ABC):
    """
        The Finder interface is what the processor uses to locate photos.
        """
    IMAGE_EXTENSIONS = ('jpg', 'jpeg', 'png')

    @abstractmethod
    def next_unprocessed_photo(self) -> Optional[Photo]:
        """ Get the next photo for processing """
        pass

    @abstractmethod
    def group_photos(self, left: Photo, right: Photo):
        """ Associate two photos - these are often the front and back of a postcard or multiple pages """
        pass

    @abstractmethod
    def set_photo_title(self, photo: Photo, title: str):
        """ Set a photo title """
        pass

    @abstractmethod
    def save_processed_image(self, photo: Photo, data: bytes):
        """ Save the processed image """
        pass