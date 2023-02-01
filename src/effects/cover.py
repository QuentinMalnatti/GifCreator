# Internal libs
from src.effects.abstract_effect import AbstractEffect

# External libs
import copy
import numpy as np


class Cover(AbstractEffect):

    def __init__(self):
        super().__init__()
        self.__step = 5
        self.__ij_done = None

    def apply_on(self, pattern):
        self.__ij_done = self._compute_1value_matrix(pattern["pattern"], 0)

        matrix = self.__compute_first_image(pattern["pattern"])
        list_img = [self._to_image(matrix, pattern["colors"]).content]

        ij_iter = self.__get_first_pixel()
        while len(self.__ij_done[self.__ij_done == 0]) != 0:
            matrix, ij_iter = self.__compute_next_image(matrix, pattern["pattern"], ij_iter)
            list_img += [self._to_image(matrix, pattern["colors"]).content]
            self._cpt += 1
        print(f"{self._cpt} iterations")
        return list_img

    @staticmethod
    def __get_first_pixel():
        return np.array([[150], [150]])

    def __compute_first_image(self, pattern):
        matrix = self._compute_1value_matrix(pattern)
        coord_0 = self.__get_first_pixel()
        matrix[coord_0[0], coord_0[1]] = pattern[coord_0[0], coord_0[1]]
        self.__ij_done[coord_0[0], coord_0[1]] += 1
        return matrix

    def __compute_next_image(self, current_matrix, pattern_matrix, ij_iter):
        next_matrix = copy.deepcopy(current_matrix)

        i_iter, j_iter = ij_iter[0], ij_iter[1]

        new_i, new_j = np.array([], dtype=int), np.array([], dtype=int)
        for i_step in np.arange(-self.__step, self.__step + 1):
            for j_step in np.arange(-self.__step, self.__step + 1):
                if [i_step, j_step] != [0, 0]:
                    new_i = np.append(new_i, i_iter + i_step)
                    new_j = np.append(new_j, j_iter + j_step)

        cond_i = ((new_i >= 0) & (new_i < len(pattern_matrix)))
        cond_j = ((new_j >= 0) & (new_j < len(pattern_matrix[0])))
        new_i = new_i[cond_i & cond_j]
        new_j = new_j[cond_i & cond_j]

        self.__ij_done[self.__ij_done > 0] += 1
        self.__ij_done[new_i, new_j] += 1  # cells with value 1 are new ones

        next_ij = np.where(self.__ij_done == 1)
        next_ij = np.array([next_ij[0], next_ij[1]])
        next_matrix[next_ij[0], next_ij[1]] = pattern_matrix[next_ij[0], next_ij[1]]

        return next_matrix, next_ij
