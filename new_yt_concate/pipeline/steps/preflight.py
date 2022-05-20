import os

from new_yt_concate.pipeline.steps.initialize_logging import logging
from new_yt_concate.settings import DOWNLOADS_DIR
from new_yt_concate.settings import VIDEOS_DIR
from new_yt_concate.settings import CAPTIONS_DIR
from new_yt_concate.settings import OUTPUT_DIR
from new_yt_concate.pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data):
        print()
        logging.info('In Preflight')
        self.create_dir()
        return None

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)