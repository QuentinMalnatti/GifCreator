# Internal libs
from components.creators.image import Img

# External libs
import numpy as np
import copy


class MatrixTools(object):

    @staticmethod
    def to_image(matrix: np.array, *args) -> Img:
        return Img(copy.deepcopy(matrix), args)

    @staticmethod
    def compute_1value_matrix(from_matrix: np.array, value=0) -> np.array:
        matrix = np.array([value] * (len(from_matrix) * len(from_matrix[0])))
        return matrix.reshape(len(from_matrix), len(from_matrix[0]))
