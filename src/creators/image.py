from PIL import Image
import numpy as np


class Img(object):

    def __init__(self, matrix, *args):
        if len(matrix[0][0]) == 3:
            self.__content = self.__create_from_rgb(matrix)
        else:
            self.__content = self.__create_from_pattern(matrix, colors=args)

    @property
    def content(self):
        return self.__content

    @classmethod
    def __create_from_rgb(cls, matrix_rgb):
        matrix = matrix_rgb.astype(np.uint8)
        return Image.fromarray(matrix)

    def __create_from_pattern(self, matrix_p, colors):
        matrix_p = matrix_p.tolist()
        matrix = self.__pattern_to_matrix(matrix_p, colors)
        matrix = np.array(matrix, dtype=np.uint8)
        return Image.fromarray(matrix)

    @staticmethod
    def __pattern_to_matrix(matrix_p, colors):
        matrix = matrix_p.copy()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                matrix[i][j] = tuple(colors[str(matrix[i][j])])

        return matrix
