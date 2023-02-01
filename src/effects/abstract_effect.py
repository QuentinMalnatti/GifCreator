# External libs
import numpy as np
import copy

# Internal libs
from src.creators.image import Img


class AbstractEffect(object):

    def __init__(self):
        self._cpt = 0
        self._main_value = 1
        self._least_value = 0

    def apply_on(self, base_image):
        raise NotImplementedError

    @staticmethod
    def _to_image(matrix, colors):
        return Img(copy.deepcopy(matrix.tolist()), colors)

    def _compute_1value_matrix(self, from_matrix, value=None):
        if value is None:
            value = self._least_value

        matrix = np.array([value]*(len(from_matrix)*len(from_matrix[0])))
        return matrix.reshape(len(from_matrix), len(from_matrix[0]))
