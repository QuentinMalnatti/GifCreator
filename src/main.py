# Internal libs
from src.creators.gif import Gif
from src.effects.draw import Draw
from src.effects.cover import Cover

# External libs
import os


class Run(object):

    PATH = os.path.dirname(os.path.realpath(__file__))
    PATTERNS_PATH = os.path.abspath(os.path.join(PATH, "..", "patterns_collection"))
    GIFS_PATH = os.path.abspath(os.path.join(PATH, "..", "gifs"))

    EFFECTS = {
        "draw": Draw,
        "cover": Cover
    }

    def __init__(self, pattern_file, effect_name, gif_file):
        pattern_file_path = os.path.abspath(os.path.join(self.PATTERNS_PATH, pattern_file))
        effect = self.EFFECTS[effect_name]
        gif_file_path = os.path.abspath(os.path.join(self.GIFS_PATH, gif_file))

        self.__gif = Gif(pattern_file_path, effect)
        self.__gif.save(gif_file_path)


if __name__ == "__main__":
    Run("tennis_court.json", "draw", "tennis_court_draw.gif")
    Run("tennis_court.json", "cover", "tennis_court_cover.gif")
