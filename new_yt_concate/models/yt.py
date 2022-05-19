import os

from new_yt_concate.settings import CAPTIONS_DIR
from new_yt_concate.settings import VIDEOS_DIR

class YT:
    def __init__(self, url):
        self.url = url
        self.id = url.split('watch?v=')[1]
        self.caption_path = os.path.join(CAPTIONS_DIR, self.id + '.txt')
        self.caption_file_exists = os.path.exists(self.caption_path) and os.path.getsize(self.caption_path) > 0
        self.video_path = os.path.join(VIDEOS_DIR, self.id + '.mp4')
        self.video_file_exists = os.path.exists(self.video_path) and os.path.getsize(self.video_path) > 0
        self.captions = None

