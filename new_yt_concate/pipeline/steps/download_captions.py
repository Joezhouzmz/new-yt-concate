import os

from pytube import YouTube

from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.pipeline.steps.step import StepException

class DownloadCaptions(Step):
    def process(self, data):
        yt_list = data
        for yt in yt_list:
            if yt.caption_file_exists:
                print('Found existing caption file', yt.id)
                continue
            source = YouTube(yt.url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt =(en_caption.generate_srt_captions())

            #save the caption to a file named Output.txt
            text_file = open(yt.caption_path, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return yt_list
