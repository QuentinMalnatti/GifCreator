# External libs
from datetime import datetime


class TimeTools(object):

    @staticmethod
    def get_delta_time(start_time):
        return datetime.now() - start_time

    @classmethod
    def get_delta_time_str(cls, start_time):
        delta_time_str = str(cls.get_delta_time(start_time)).split(':')
        return f"{delta_time_str[0]}h{delta_time_str[1]}m{delta_time_str[2]}s"

