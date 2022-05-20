from pytube import YouTube
from pytube.exceptions import RegexMatchError

from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.settings import VIDEOS_DIR
from new_yt_concate.pipeline.steps.initialize_logging import logging

class DownloadVideos(Step):
    def process(self, data):
        yt_downloading_set = set([target_caption.yt for target_caption in data])
        logging.info('num of videos to download: '+ str(len(yt_downloading_set)))
        for yt in yt_downloading_set:
            url = yt.url
            if yt.video_file_exists:
                logging.info(f'found existing video file --{url}--skipping')
                continue
            
            try:
                logging.info('downloading '+url)
                YouTube(url).streams.get_by_itag(18).download(output_path=VIDEOS_DIR, filename=yt.id+'.mp4')
            except RegexMatchError:
                logging.info('found error RegexMatchError, skipping')

        return data