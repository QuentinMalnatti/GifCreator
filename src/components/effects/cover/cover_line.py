# Internal libs
from components.effects.cover.abstract_cover import AbstractCover

# External libs
import numpy as np


class CoverLine(AbstractCover):

    def _get_first_pixel(self, matrix):
        raise NotImplementedError

    def _is_good_step(self, step):
        return step != [0, 0]


class CoverLineLeft(CoverLine):

    def _get_first_pixel(self, matrix):
        return np.array([list(np.arange(0, len(matrix))), list(np.array([0] * len(matrix)))])


class CoverLineTop(CoverLine):

    def _get_first_pixel(self, matrix):
        return np.array([list(np.array([0] * len(matrix[0]))), list(np.arange(0, len(matrix[0])))])


class CoverLineRight(CoverLine):

    def _get_first_pixel(self, matrix):
        return np.array([list(np.arange(0, len(matrix))), list(np.array([len(matrix)-1] * len(matrix)))])


class CoverLineBottom(CoverLine):

    def _get_first_pixel(self, matrix):
        return np.array([list(np.array([len(matrix[0])-1] * len(matrix[0]))), list(np.arange(0, len(matrix[0])))])
