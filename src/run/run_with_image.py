# Internal libs
from run.abstract_run import AbstractRun
from utils.file_tools import FileTools

# External libs
import os
import numpy as np
from PIL import Image


class RunWithImage(AbstractRun):

    def __init__(self, image_file: str, effect_name: str, save: bool = False):
        super().__init__(image_file, effect_name, save)

    @classmethod
    def _define_input_path(cls, image_file: str) -> str:
        image_path = os.path.abspath(os.path.join(cls.DATA_PATH, "in", "images"))
        return os.path.abspath(os.path.join(image_path, image_file))

    @classmethod
    def _extract_pattern(cls, image_file_path: str) -> dict:
        image = FileTools.read_image(image_file_path)
        return cls.__image_to_pattern(image)

    @staticmethod
    def __image_to_pattern(image: Image) -> dict:
        pattern = {
            "image": None,
            "image_binary": None,
            "pattern": None,
            "colors": {
                "0": [0, 0, 0],
                "1": [255, 255, 255]
            }
        }

        image = image.resize((200, 200))
        image = image.convert("RGB")
        pattern["image"] = np.array(image)

        image = image.convert('L')
        image = image.point(lambda p: 255 if p > 255 / 2 else 0)
        pattern["pattern"] = np.array(image.point(lambda p: 1 if p > 255 / 2 else 0))

        image = image.convert("RGB")
        pattern["image_binary"] = np.array(image)

        return pattern
