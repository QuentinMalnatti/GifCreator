# Internal libs
from src.utils.file_tools import FileTools


class Gif(object):

    def __init__(self, pattern_file, effect):
        pattern = FileTools.read_json(pattern_file)
        self.__content = effect().apply_on(pattern)

    def save(self, gif_file):
        self.__content[0].save(gif_file, save_all=True, append_images=self.__content[1:], optimize=False, duration=100, loop=0)
