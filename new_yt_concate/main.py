
from new_yt_concate.pipeline.pipeline import Pipeline
from new_yt_concate.pipeline.steps.initialize_logging import InitializeLogging
from new_yt_concate.pipeline.steps.preflight import Preflight
from new_yt_concate.pipeline.steps.get_video_list import GetVideoList
from new_yt_concate.pipeline.steps.initialize_yt import InitializeYT
from new_yt_concate.pipeline.steps.download_captions import DownloadCaptions
from new_yt_concate.pipeline.steps.read_captions import ReadCaptions
from new_yt_concate.pipeline.steps.search import Search
from new_yt_concate.pipeline.steps.download_videos import DownloadVideos
from new_yt_concate.pipeline.steps.edit_video import EditVideo
from new_yt_concate.pipeline.steps.postflight import Postflight

def main():
    steps = [
        InitializeLogging(),
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]
    p = Pipeline(steps)
    p.run()

if __name__ == '__main__':
    main()