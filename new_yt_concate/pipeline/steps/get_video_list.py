import os
import urllib.request
import json

from new_yt_concate.settings import API_KEY, use_existing_video_links_file, VIDEO_LINK_FILE_DIR
from new_yt_concate.settings import channel_id
from new_yt_concate.settings import video_link_number
from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.pipeline.steps.initialize_logging import logging


class GetVideoList(Step):
    def process(self, data):
        if use_existing_video_links_file:
            if os.path.exists(VIDEO_LINK_FILE_DIR):
                logging.info('Using existing video links file')
                self.read_video_links_file()
            else:
                logging.info('No existing video links file. Creating new video links file')
        else:
            if os.path.exists(VIDEO_LINK_FILE_DIR):
                logging.info('Found existing video links file. Deleting and creating new video links file')
                os.remove(VIDEO_LINK_FILE_DIR)
            else:
                logging.info('Creating new video links file')

        api_key = API_KEY

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        reach_video_links_number_limit = False

        while not reach_video_links_number_limit:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

                if len(video_links) >= video_link_number:
                    reach_video_links_number_limit = True
                    break

        logging.info('video links: '+ str(video_links))
        logging.info('the len of video_links'+ str(len(video_links)))
        self.write_video_links_to_file(video_links)
        return video_links

    @staticmethod
    def write_video_links_to_file(video_links):
        with open(VIDEO_LINK_FILE_DIR, 'w') as f:
            for url in video_links:
                f.write(url+'\n')

    @staticmethod
    def read_video_links_file():
        video_links = []
        with open(VIDEO_LINK_FILE_DIR, 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links
