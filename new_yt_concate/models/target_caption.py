
class TargetCaption:
    def __init__(self, yt, caption, time_str):
        self.yt = yt
        self.caption = caption
        self.time_str = time_str
        self.starting_time_str, self.ending_time_str = self.parse_caption_time()

    def __str__(self):
        return 'Found search word "' + self.caption + '" at time ' + self.time_str

    def parse_caption_time(self):
        starting_time_str, ending_time_str = self.time_str.split(' --> ')
        return self.parse_time_str(starting_time_str), self.parse_time_str(ending_time_str)

    @staticmethod
    def parse_time_str(time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms ) /1000
