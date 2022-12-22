# Internal libs
from src.utils.file_tools import FileTools

# External libs
from PIL import Image
import numpy as np


class Img(object):

    def __init__(self, pattern_file):
        pattern = FileTools.read_json(pattern_file)
        self.__content = self.__create_from_pattern(pattern)

    @property
    def content(self):
        return self.__content

    def __create_from_pattern(self, pattern):
        matrix = self.__pattern_to_matrix(pattern)
        matrix = np.array(matrix, dtype=np.uint8)
        return Image.fromarray(matrix)

    @staticmethod
    def __pattern_to_matrix(pattern):
        matrix = pattern["image"]
        colors = pattern["colors"]

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                matrix[i][j] = tuple(colors[str(matrix[i][j])])

        return matrix
