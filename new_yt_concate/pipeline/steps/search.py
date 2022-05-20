from new_yt_concate.settings import search_word
from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.models.target_caption import TargetCaption
from new_yt_concate.pipeline.steps.initialize_logging import logging

class Search(Step):
    def process(self, data):
        logging.info('searching for target captions')
        target_captions_list = []
        for yt in data:
            if yt.captions:
                captions = yt.captions
                for caption in captions:
                    if search_word in caption:
                        time_str = captions[caption]
                        tc = TargetCaption(yt, caption, time_str)
                        target_captions_list.append(tc)
                        logging.info(tc)
        logging.info('the len of target_captions_list is '+ str(len(target_captions_list)))
        return target_captions_list