from new_yt_concate.pipeline.steps.step import Step

class Postflight(Step):
    def process(self, data):
        print('In Postflight')