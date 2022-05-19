import os

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.settings import OUTPUT_DIR
from new_yt_concate.settings import channel_id
from new_yt_concate.settings import search_word

class EditVideo(Step):
    def process(self, data):
        target_video_clips = []
        for target_caption in data:
            video = VideoFileClip(target_caption.yt.video_path).subclip(target_caption.starting_time_str, target_caption.ending_time_str)
            target_video_clips.append(video)

        print(target_video_clips)
        final_clip = concatenate_videoclips(target_video_clips)
        final_clip.write_videofile(os.path.join(OUTPUT_DIR, search_word+'_'+channel_id+'.mp4'), threads=4, codec='libx264')

        return final_clip