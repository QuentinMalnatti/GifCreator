# Internal libs
from components.effects.cover.abstract_cover import AbstractCover

# External libs
import numpy as np


class CoverDiag(AbstractCover):

    def _get_first_pixel(self, matrix):
        raise NotImplementedError

    def _is_good_step(self, step):
        return (step != [0, 0]) & (abs(step[0]) + abs(step[1]) <= self._step)


class CoverDiagTopLeft(CoverDiag):

    def _get_first_pixel(self, matrix):
        return np.array([[0, 0, 1], [0, 1, 0]])


class CoverDiagBottomLeft(CoverDiag):

    def _get_first_pixel(self, matrix):
        return np.array([[len(matrix)-1, len(matrix)-1, len(matrix)-2], [0, 1, 0]])


class CoverDiagBottomRight(CoverDiag):

    def _get_first_pixel(self, matrix):
        return np.array([[len(matrix)-1, len(matrix)-1, len(matrix)-2], [len(matrix[0])-1, len(matrix[0])-2, len(matrix[0])-1]])


class CoverDiagTopRight(CoverDiag):

    def _get_first_pixel(self, matrix):
        return np.array([[0, 0, 1], [len(matrix[0])-1, len(matrix[0])-2, len(matrix[0])-1]])
