import os

from dotenv import load_dotenv
load_dotenv()

search_word = 'insane'
video_link_number = 4
use_existing_video_links_file = True

API_KEY = os.getenv('API_KEY')
CHANNEL_ID = 'UCq5ZYJax8VC580PAIU5xuvg'
DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'cations')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
VIDEO_LINK_FILE_DIR = os.path.join(DOWNLOADS_DIR, CHANNEL_ID+'txt')