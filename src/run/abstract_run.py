# Internal libs
from components.creators.gif import Gif
# Effects
from components.effects.cover.covers import CoverLine

# External libs
import os
from datetime import datetime


class AbstractRun(object):

    PATH = os.path.dirname(os.path.realpath(__file__))
    DATA_PATH = os.path.abspath(os.path.join(PATH, "..", "..", "data"))
    GIFS_PATH = os.path.abspath(os.path.join(DATA_PATH, "out", "gifs"))

    EFFECTS = {
        "cover_line": CoverLine,
    }

    def __init__(self, intput_file: str, effect_name: str, save: bool = False):
        input_file_path = self._define_input_path(intput_file)
        effect = self.EFFECTS[effect_name]
        gif_file = self.__define_gif_file(intput_file, effect_name)
        gif_file_path = os.path.abspath(os.path.join(self.GIFS_PATH, gif_file))

        print("- Start")
        print("-- Extract pattern...")
        pattern = self._extract_pattern(input_file_path)
        print(f"-- Effect {effect_name}...")
        start_time = datetime.now()
        self.__gif = Gif(pattern, effect)
        delta_time = str(datetime.now() - start_time).split(':')
        print(f"Execution time : {delta_time[0]}h{delta_time[1]}m{delta_time[2]}s")
        if save:
            print("-- Save...")
            self.__gif.save(gif_file_path)
        print("- End")
        print()

    @classmethod
    def _define_input_path(cls, input_file: str) -> str:
        raise NotImplementedError

    @staticmethod
    def __define_gif_file(input_file: str, effect_name: str) -> str:
        return f"{input_file.split('.')[0]}_{effect_name}.gif"

    @staticmethod
    def _extract_pattern(input_file_path: str) -> dict:
        raise NotImplementedError
