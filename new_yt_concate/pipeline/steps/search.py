

from new_yt_concate.settings import search_word
from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.models.target_caption import TargetCaption

class Search(Step):
    def process(self, data):
        target_captions_list = []
        for yt in data:
            if yt.captions:
                captions = yt.captions
                for caption in captions:
                    if search_word in caption:
                        time_str = captions[caption]
                        tc = TargetCaption(yt, caption, time_str)
                        target_captions_list.append(tc)
                        print(tc)
        print(len(target_captions_list))
        return target_captions_list