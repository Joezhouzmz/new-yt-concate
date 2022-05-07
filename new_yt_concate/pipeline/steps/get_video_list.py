import os
import urllib.request
import json

from new_yt_concate.settings import API_KEY, use_existing_video_links_file, VIDEO_LINK_FILE_DIR
from new_yt_concate.settings import CHANNEL_ID
from new_yt_concate.settings import video_link_number
from new_yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self, data):
        if not self.check_if_rewrite_video_links_list():
            print('Using old video links file')
            return self.read_video_links_file()

        print('Creating new video links file')

        channel_id = CHANNEL_ID
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

        print(video_links)
        print(len(video_links))
        self.write_video_links_to_file(video_links)
        return video_links

    @staticmethod
    def check_if_rewrite_video_links_list():
        if not use_existing_video_links_file:
            return True
        else:
            return not os.path.exists(VIDEO_LINK_FILE_DIR)

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