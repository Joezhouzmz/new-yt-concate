from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.pipeline.steps.initialize_logging import logging

class Postflight(Step):
    def process(self, data):
        logging.info('In Postflight')