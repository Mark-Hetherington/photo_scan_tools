from typing import List

from finder.base import Finder, Photo
from handlers.base import PhotoHandler
from interfaces.logging import LoggingProtocol


class PhotoProcessor:
    handlers: List[PhotoHandler]

    def __init__(self, finder: Finder, logger: LoggingProtocol):
        self.finder = finder
        self.logger = logger

    def process(self):
        self.logger.info("Beginning processing")
        while photo := self.finder.next_unprocessed_photo():
            self.process_photo(photo)

    def process_photo(self, photo: Photo):
        for handler in self.handlers:
            if handler.can_process(photo):
                handler.process(photo)
