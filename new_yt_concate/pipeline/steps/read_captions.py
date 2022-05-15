

from new_yt_concate.pipeline.steps.step import Step

class ReadCaptions(Step):
    def process(self, data):

        for yt in data:
            if not yt.caption_file_exists:
                continue

            one_video_caption_dict = {}
            with open(yt.caption_path, 'r') as f:
                this_line_is_time = False
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        this_line_is_time = True
                        time_line = line
                        continue
                    if this_line_is_time:
                        one_video_caption_dict[line] = time_line
                        this_line_is_time = False

            yt.captions = one_video_caption_dict

        return data