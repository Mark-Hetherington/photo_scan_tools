from abc import ABC, abstractmethod

from finder.base import Photo


class PhotoHandler(ABC):
    @abstractmethod
    def can_process(self, photo: Photo):
        pass

    @abstractmethod
    def process(self, photo: Photo):
        pass

