from abc import ABC, abstractmethod

from finder.base import Photo, Finder


class PhotoHandler(ABC):
    @abstractmethod
    def process(self, photo: Photo, finder: Finder):
        pass

