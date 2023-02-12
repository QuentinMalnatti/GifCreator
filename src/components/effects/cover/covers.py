# Internal libs
from components.effects.cover.abstract_cover import AbstractCover

# External libs
import numpy as np


class CoverLine(AbstractCover):

    def _get_first_pixel(self, matrix):
        return np.array([list(np.arange(0, len(matrix))), list(np.array([0] * len(matrix)))])

