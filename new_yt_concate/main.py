# UCJFN9Mo4AMR_qZ1ZB6i2N8Q


from new_yt_concate.pipeline.pipeline import Pipeline
from new_yt_concate.pipeline.steps.preflight import Preflight
from new_yt_concate.pipeline.steps.get_video_list import GetVideoList
from new_yt_concate.pipeline.steps.initialize_yt import InitializeYT
from new_yt_concate.pipeline.steps.download_captions import DownloadCaptions
from new_yt_concate.pipeline.steps.read_captions import ReadCaptions
from new_yt_concate.pipeline.steps.search import Search
from new_yt_concate.pipeline.steps.postflight import Postflight

def main():
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        Postflight(),
    ]
    p = Pipeline(steps)
    p.run()

if __name__ == '__main__':
    main()