from src.creators.image import Img


class Gif(object):

    def __init__(self, pattern_file, effect=None):
        base_image = Img(pattern_file)
        self.__content = None
