import dataclasses
import json
from itertools import chain
from pathlib import Path
from typing import List, Optional

from finder.base import Finder, Photo, Frame
from interfaces.logging import LoggingProtocol


class FilesystemFinder(Finder):
    """ Finds files on disk and stores metadata in json files """

    def __init__(self, source: str, destination: str, logger: LoggingProtocol):
        self.source = Path(source)
        self.destination = Path(destination)
        self.metadata: List[Photo] = []
        self.logger = logger

        self._create_json_from_images()
        self._load_json_files()

    def _get_source_path(self, path: str):
        return self.source / path

    def _save_metadata(self, photo: Photo):
        json.dump(dataclasses.asdict(photo), open(self._get_source_path(photo.metadata_location), "w"))

    def _delete_metadata(self, photo: Photo):
        path: Path = self._get_source_path(photo.metadata_location)
        path.unlink()

    def group_photos(self, left: Photo, right: Photo):
        left.frames.extend(right.frames)
        self.metadata.remove(right)
        self.logger.debug(f"Added {right.location()} to {left.location()}")

    def set_photo_title(self, photo: Photo, title: str):
        photo.title = title

    def save_processed_image(self, photo: Photo, data: bytes):
        pass

    def _create_json_from_images(self):
        """ Finds image files, and creates a metadata file for them """
        globs = (self.source.glob(f"**/*.{extension}") for extension in self.IMAGE_EXTENSIONS)
        for path in chain(*globs):
            metadata_location = path.with_suffix(".json")
            if metadata_location.exists():
                continue
            title = path.stem
            photo = Photo(metadata_location=str(metadata_location), title=title, frames=[Frame(location=str(path))])
            self._save_metadata(photo)
            self.logger.debug(f"Creating JSON file for {path}")

    def _load_json_files(self):
        """ Loads all the JSON files as data """

        for path in self.source.glob("**/*.json"):
            data = json.load(open(path))
            photo = Photo(**data)
            photo.frames = [Frame(**frame) for frame in photo.frames]
            self.logger.debug(f"Loading metadata for {path}")
            self.metadata.append(photo)

    def _unprocessed_photos(self):
        return (photo for photo in self.metadata if not photo.processed)

    def next_unprocessed_photo(self) -> Optional[Photo]:
        return next(self._unprocessed_photos(), None)

    def get_photo_by_location(self, location: str) -> Optional[Photo]:
        for photo in self.metadata:
            for frame in photo.frames:
                if frame.location == location:
                    return photo
        return None
