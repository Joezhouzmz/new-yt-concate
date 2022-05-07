import os


from new_yt_concate.settings import CAPTIONS_DIR

def get_video_id_from_url(url):
    return url.split('watch?v=')[1]

def get_caption_path(url):
    return os.path.join(CAPTIONS_DIR, get_video_id_from_url(url) + '.txt')

def caption_file_exists(url):
    path = get_caption_path(url)
    return os.path.exists(path) and os.path.getsize(path) > 0
