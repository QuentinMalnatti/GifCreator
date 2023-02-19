# Internal libs
from run.abstract_run import AbstractRun
from utils.file_tools import FileTools

# External libs
import os
import numpy as np


class RunWithPattern(AbstractRun):

    def __init__(self, pattern_file: str, effect_name: str, save: bool = False):
        super().__init__(pattern_file, effect_name, save)

    @classmethod
    def _define_input_path(cls, pattern_file: str) -> str:
        patterns_path = os.path.abspath(os.path.join(cls.DATA_PATH, "in", "patterns"))
        return os.path.abspath(os.path.join(patterns_path, pattern_file))

    @staticmethod
    def _extract_pattern(pattern_file_path: str) -> dict:
        pattern = FileTools.read_json(pattern_file_path)
        for elmnts in ["image", "image_binary", "pattern"]:
            pattern[elmnts] = np.array(pattern[elmnts])
        return pattern
