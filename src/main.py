# Internal libs
from src.creators.gif import Gif

# External libs
import os


class Run(object):

    PATH = os.path.dirname(os.path.realpath(__file__))
    PATTERNS_PATH = os.path.abspath(os.path.join(PATH, "..", "patterns_collection"))

    EFFECTS = {}

    def __init__(self, pattern_file, effect_name):
        pattern_file_path = os.path.abspath(os.path.join(self.PATTERNS_PATH, pattern_file))
        effect = None #self.EFFECTS[effect_name]

        self.__gif = Gif(pattern_file_path, effect)


if __name__ == "__main__":
    Run("tennis_court.json", None)
