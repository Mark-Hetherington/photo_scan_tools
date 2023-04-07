import argparse
import logging

from finder.filesystem import FilesystemFinder
from handlers.annotation import AnnotationHandler
from handlers.multiframe import MultiframeHandler
from processor import PhotoProcessor

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("source")
parser.add_argument("destination")
args = parser.parse_args()

print(f"Processing photos in {args.source} and saving to {args.destination}")
finder = FilesystemFinder(source=args.source, destination=args.destination, logger=logging)

handlers = [MultiframeHandler(), AnnotationHandler()]

processor = PhotoProcessor(finder=finder, logger=logging, handlers=handlers)
processor.process()
