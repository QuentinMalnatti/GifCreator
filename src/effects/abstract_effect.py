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

    def _compute_background(self, base_image):
        """
        row = list()
        for j in range(0, len(base_image["pattern"][0])):
            row.append(self._least_value)

        matrix = list()
        for i in range(0, len(base_image["pattern"])):
            matrix.append(row.copy())

        return matrix
        """
        matrix = np.array([self._least_value]*(len(base_image["pattern"])*len(base_image["pattern"][0])))
        return matrix.reshape(len(base_image["pattern"]), len(base_image["pattern"][0]))
