
from new_yt_concate.pipeline.steps.step import Step
from new_yt_concate.models.yt import YT

class InitializeYT(Step):
    def process(self, data):
        return [YT(url) for url in data]