# Internal libs
import numpy as np

from utils.matrix_tools import MatrixTools

# External libs
from typing import Any
from PIL import Image

class AbstractEffect(object):

    matrix_tools = MatrixTools

    def __init__(self):
        self.__cpt = 0
        self.__list_img = None

    def apply_on(self, base_image: dict) -> list[Image]:
        iter_components = self._init(base_image)
        matrix = self._compute_first_image(base_image)
        self.__list_img = [self.matrix_tools.to_image(matrix).content]

        while not self._is_finish():
            matrix, iter_components = self._compute_next_image(matrix, base_image, iter_components)
            self.__list_img += [self.matrix_tools.to_image(matrix).content]
            self.__cpt += 1
        print(f"{self.__cpt} iterations")
        return self.__list_img

    def _init(self, base_image: dict) -> dict:
        raise NotImplementedError

    def _compute_first_image(self, base_image: dict) -> np.array:
        raise NotImplementedError

    def _is_finish(self) -> bool:
        raise NotImplementedError

    def _compute_next_image(self, matrix: np.array, base_image: dict, iter_components: dict) -> tuple[np.array, dict]:
        raise NotImplementedError
