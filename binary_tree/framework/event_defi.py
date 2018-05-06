class Event:
    def __init__(self, event_time, host):
        self._ctime = event_time  # 事件发生的时间
        self._host = host  # 事件发生所在的模拟系统

    def __lt__(self, other_event):
        return self._ctime < other_event._ctime

    def __le(self, other_event):
        return self._ctime <= other_event._ctime

    def hout(self):
        return self._host

    def time(self):
        return self._ctime

    def run(self):
        pass
