# Internal libs
from src.effects.abstract_effect import AbstractEffect

# External libs
import copy


class Draw(AbstractEffect):

    def __init__(self):
        super().__init__()

    def apply_on(self, pattern):
        matrix = self.__compute_first_image(pattern)
        list_img = [self._to_image(copy.deepcopy(matrix), pattern["colors"]).content]

        is_finish, matrix = self.__compute_next_image(matrix, pattern["pattern"])
        while not is_finish:
            list_img.append(self._to_image(copy.deepcopy(matrix), pattern["colors"]).content)
            is_finish, matrix = self.__compute_next_image(matrix, pattern["pattern"])

        return list_img

    def __compute_first_image(self, pattern):
        matrix = self._compute_1value_matrix(pattern["pattern"])
        i0, j0 = self.__detect_first_pixel(pattern["pattern"])
        matrix[i0][j0] = self._main_value
        return matrix

    def __detect_first_pixel(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == self._main_value:
                    return i, j

    def __compute_next_image(self, current_matrix, pattern_matrix):
        next_matrix = copy.deepcopy(current_matrix)
        for i in range(0, len(current_matrix)):
            for j in range(0, len(current_matrix[0])):
                if current_matrix[i][j] == self._main_value:
                    next_matrix = self.__update_matrix(next_matrix, pattern_matrix, i, j)

        if next_matrix == current_matrix:
            return True, None
        else:
            return False, next_matrix

    @staticmethod
    def __update_matrix(next_matrix, pattern_matrix, i, j):
        for y_step in [0, -1, 1]:
            for x_step in [0, -1, 1]:
                next_matrix[i + y_step][j + x_step] = pattern_matrix[i + y_step][j + x_step]

        return next_matrix
