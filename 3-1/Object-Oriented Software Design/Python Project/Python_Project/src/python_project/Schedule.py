class Schedule:

    def __init__(self, day, start_time, end_time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    def compare(self, schedule):
        if self.day == schedule.day:
            if (self.end_time > schedule.start_time >= self.start_time) or (
                    self.end_time >= schedule.end_time > self.start_time):
                return True
            elif schedule.start_time < self.start_time and schedule.end_time > self.end_time:
                return True
        return False

    def __str__(self) -> str:
        return f'day={self.day}, start_time={self.start_time}, end_time={self.end_time}'

    def __repr__(self) -> str:
        return f'day={self.day}, start_time={self.start_time}, end_time={self.end_time}'

