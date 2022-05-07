import os

from pytube import YouTube

from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.pipeline.steps.step import StepException
from new_yt_concate.utils import get_caption_path
from new_yt_concate.utils import get_video_id_from_url
from new_yt_concate.utils import caption_file_exists

class DownloadCaptions(Step):
    def process(self, data):
        video_list = data
        for url in video_list:
            if caption_file_exists(url):
                print('Found existing caption file', get_video_id_from_url(url))
                continue
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt =(en_caption.generate_srt_captions())

            #save the caption to a file named Output.txt
            text_file = open(get_caption_path(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()



