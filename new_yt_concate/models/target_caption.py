

class TargetCaption:
    def __init__(self, yt, caption, time_str):
        self.yt = yt
        self.caption = caption
        self.time_str = time_str

    def __str__(self):
        return 'Found search word "' + self.caption + '" at time ' + self.time_str
