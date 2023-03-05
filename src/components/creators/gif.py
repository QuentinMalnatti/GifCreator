from components.creators.image import Img
from components.effects.abstract_effect import AbstractEffect


class Gif(object):

    def __init__(self, pattern: dict, effect: AbstractEffect.__subclasses__()):
        self.__content = effect().apply_on(pattern)

    def save(self, gif_file: str) -> None:
        self.__content[0].save(gif_file, save_all=True, append_images=self.__content[1:], optimize=False, duration=75, loop=0)
