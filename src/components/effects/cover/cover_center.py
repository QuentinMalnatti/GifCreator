# Internal libs
from components.effects.cover.abstract_cover import AbstractCover

# External libs
import numpy as np


class CoverCenter(AbstractCover):

    def _get_first_pixel(self, matrix):
        return np.array([[round(len(matrix)/2)], [round(len(matrix[0])/2)]])

    def _is_good_step(self, step):
        return step != [0, 0]
