import os

from dotenv import load_dotenv
load_dotenv()

channel_id = 'UCq5ZYJax8VC580PAIU5xuvg'
search_word = 'papaya'
video_link_number = 20
use_existing_video_links_file = True

API_KEY = os.getenv('API_KEY')
DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
VIDEO_LINK_FILE_DIR = os.path.join(DOWNLOADS_DIR, channel_id + '.txt')
OUTPUT_DIR = 'output'