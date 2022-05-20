import logging
import sys

from new_yt_concate.pipeline.steps.step import Step


class InitializeLogging(Step):
    def process(self, data):
        logger = self.create_logger()
        logger.info('logger initialized')
        self.logger = logger
        return None


    def create_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(filename)s - %(message)s')

        file_handler = logging.FileHandler('new_yt_concate.log')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger


