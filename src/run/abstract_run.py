# Internal libs
from components.creators.gif import Gif
from utils.time_tools import TimeTools
# Effects
from components.effects.cover.cover_line import CoverLineLeft, CoverLineRight, CoverLineTop, CoverLineBottom
from components.effects.cover.cover_diag import CoverDiagTopLeft, CoverDiagTopRight, CoverDiagBottomLeft, CoverDiagBottomRight
# External libs
import os
from datetime import datetime


class AbstractRun(object):

    PATH = os.path.dirname(os.path.realpath(__file__))
    DATA_PATH = os.path.abspath(os.path.join(PATH, "..", "..", "data"))
    GIFS_PATH = os.path.abspath(os.path.join(DATA_PATH, "out", "gifs"))

    EFFECTS = {
        "cover_line_left": CoverLineLeft,
        "cover_line_right": CoverLineRight,
        "cover_line_top": CoverLineTop,
        "cover_line_bottom": CoverLineBottom,
        "cover_diag_top_left": CoverDiagTopLeft,
        "cover_diag_top_right": CoverDiagTopRight,
        "cover_diag_bottom_left": CoverDiagBottomLeft,
        "cover_diag_bottom_right": CoverDiagBottomRight
    }

    def __init__(self, intput_file: str, effect_name: str, save: bool = False):
        input_file_path = self._define_input_path(intput_file)
        effect = self.EFFECTS[effect_name]
        gif_file = self.__define_gif_file(intput_file, effect_name)
        gif_file_path = os.path.abspath(os.path.join(self.GIFS_PATH, gif_file))

        global_start_time = datetime.now()
        print("- Start")
        print("-- Extract pattern...")
        pattern = self._extract_pattern(input_file_path)
        print(f"-- Effect {effect_name}...")
        start_time = datetime.now()
        self.__gif = Gif(pattern, effect)
        print(f"Execution time : {TimeTools.get_delta_time_str(start_time)}")
        if save:
            print("-- Save...")
            self.__gif.save(gif_file_path)
        print("- End")
        print(f"Total execution time : {TimeTools.get_delta_time_str(global_start_time)}")
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
