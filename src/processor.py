from typing import List

from finder.base import Finder, Photo
from handlers.base import PhotoHandler
from interfaces.logging import LoggingProtocol


class PhotoProcessor:

    def __init__(self, finder: Finder, logger: LoggingProtocol, handlers: List[PhotoHandler]) -> None:
        self.finder = finder
        self.logger = logger
        self.handlers = handlers

    def process(self) -> None:
        self.logger.info("Beginning processing")
        while photo := self.finder.next_unprocessed_photo():
            self.process_photo(photo)

    def process_photo(self, photo: Photo) -> None:
        for handler in self.handlers:
            handler.process(photo, self.finder)
