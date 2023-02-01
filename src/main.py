# Internal libs
from src.utils.file_tools import FileTools
from src.utils.image_tools import ImageTools
from src.creators.gif import Gif
# Effects
from src.effects.draw import Draw
from src.effects.cover import Cover

# External libs
import os
from datetime import datetime
import numpy as np


class Run(object):

    PATH = os.path.dirname(os.path.realpath(__file__))
    GIFS_PATH = os.path.abspath(os.path.join(PATH, "..", "data", "out", "gifs"))

    EFFECTS = {
        "draw": Draw,
        "cover": Cover,
    }

    def __init__(self, intput_file, effect_name, save=False):
        input_file_path = self._define_input_path(intput_file)
        effect = self.EFFECTS[effect_name]
        gif_file = self._define_gif_file(intput_file, effect_name)
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
    def _define_input_path(cls, input_file):
        raise NotImplementedError

    @staticmethod
    def _define_gif_file(input_file, effect_name):
        raise NotImplementedError

    @staticmethod
    def _extract_pattern(input_file_path):
        raise NotImplementedError


class RunWithPattern(Run):

    def __init__(self, pattern_file, effect_name, save=False):
        super().__init__(pattern_file, effect_name, save)

    @classmethod
    def _define_input_path(cls, pattern_file):
        patterns_path = os.path.abspath(os.path.join(cls.PATH, "..", "data", "in", "patterns"))
        return os.path.abspath(os.path.join(patterns_path, pattern_file))

    @staticmethod
    def _define_gif_file(input_file, effect_name):
        return f"{input_file.split('.')[0]}_{effect_name}_form_pattern.gif"

    @staticmethod
    def _extract_pattern(pattern_file_path):
        pattern = FileTools.read_json(pattern_file_path)
        pattern["pattern"] = np.array(pattern["pattern"])
        return pattern


class RunWithImage(Run):

    def __init__(self, image_file, effect_name, save=False):
        super().__init__(image_file, effect_name, save)

    @classmethod
    def _define_input_path(cls, image_file):
        image_path = os.path.abspath(os.path.join(cls.PATH, "..", "data", "in", "images"))
        return os.path.abspath(os.path.join(image_path, image_file))

    @staticmethod
    def _define_gif_file(input_file, effect_name):
        return f"{input_file.split('.')[0]}_{effect_name}_form_image.gif"

    @staticmethod
    def _extract_pattern(image_file_path):
        image = FileTools.read_image(image_file_path)
        return ImageTools.image_to_pattern(image)


if __name__ == "__main__":
    #RunWithPattern("tennis_court.json", "cover", True)
    RunWithImage("tennis_court_in_forest.jpg", "cover", True)
