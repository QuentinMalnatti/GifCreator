# Internal libs
from src.effects.abstract_effect import AbstractEffect

# External libs
import copy


class Cover(AbstractEffect):

    def __init__(self):
        super().__init__()
        self.__i0, self.__j0 = self.__get_first_pixel()

    @staticmethod
    def __get_first_pixel():
        return 0, 0

    def apply_on(self, pattern):
        matrix = self.__compute_first_image(pattern)
        list_img = [self._to_image(copy.deepcopy(matrix), pattern["colors"]).content]

        i_done = [self.__i0]
        j_done = [self.__j0]
        while len(i_done) < len(pattern["pattern"]) or len(j_done) < len(pattern["pattern"][0]):
            matrix, i_done, j_done = self.__compute_next_image(matrix, pattern["pattern"], i_done, j_done)
            list_img.append(self._to_image(copy.deepcopy(matrix), pattern["colors"]).content)
        return list_img

    def __compute_first_image(self, pattern):
        matrix = self._compute_background(pattern)
        matrix[self.__i0][self.__j0] = pattern["pattern"][self.__i0][self.__j0]
        return matrix

    def __compute_next_image(self, current_matrix, pattern_matrix, i_done, j_done):
        next_matrix = copy.deepcopy(current_matrix)
        new_i_done = i_done.copy()
        new_j_done = j_done.copy()
        for i in i_done:
            for j in j_done:
                next_matrix, new_i_done, new_j_done = self.__update_matrix(next_matrix, pattern_matrix, i, j, new_i_done, new_j_done)
        return next_matrix, new_i_done, new_j_done

    @staticmethod
    def __update_matrix(next_matrix, pattern_matrix, i, j, new_i_done, new_j_done):
        for y_step in [0, -1, 1]:
            for x_step in [0, -1, 1]:
                if 0 <= i + y_step < len(pattern_matrix):
                    if 0 <= j + x_step < len(pattern_matrix[0]):
                        next_matrix[i + y_step][j + x_step] = pattern_matrix[i + y_step][j + x_step]
                        if y_step != 0 and i + y_step not in new_i_done:
                            new_i_done.append(i + y_step)
                        if x_step != 0 and j + x_step not in new_j_done:
                            new_j_done.append(j + x_step)
        return next_matrix, new_i_done, new_j_done

