# Internal libs
from src.effects.abstract_effect import AbstractEffect

# External libs
import copy
import numpy as np


class Cover2(AbstractEffect):

    def __init__(self):
        super().__init__()
        self.__step = 1
        self.__ij_done = None

    @staticmethod
    def __get_first_pixel():
        return np.array([[0, 0]])

    def apply_on(self, pattern):
        self.__ij_done = self.__get_first_pixel()
        matrix = self.__compute_first_image(pattern)
        list_img = [self._to_image(matrix, pattern["colors"]).content]

        ij_iter = self.__get_first_pixel()
        while len(self.__ij_done) < len(pattern["pattern"])*len(pattern["pattern"][0]):
            matrix, ij_iter = self.__compute_next_image(matrix, pattern["pattern"], ij_iter)
            list_img += [self._to_image(matrix, pattern["colors"]).content]
            self._cpt += 1
        print(f"{self._cpt} iterations")
        return list_img

    def __compute_first_image(self, pattern):
        matrix = self._compute_background(pattern)
        coords_0 = self.__ij_done[0, 0], self.__ij_done[0, 1]
        matrix[coords_0] = pattern["pattern"][coords_0]
        return matrix

    def __compute_next_image(self, current_matrix, pattern_matrix, ij_iter):
        next_matrix = copy.deepcopy(current_matrix)
        new_ij_iter = np.array([])
        for coord in ij_iter:
            next_matrix, new_ij_iter = self.__update_matrix(next_matrix, pattern_matrix, coord, new_ij_iter)
        self.__ij_done = np.append(self.__ij_done, new_ij_iter, axis=0)
        self.__ij_done = np.unique(self.__ij_done, axis=0)
        return next_matrix, new_ij_iter

    def __correct_min_step(self, c):
        if c - self.__step >= 0:
            return self.__step
        else:
            return c

    def __correct_max_step(self, c, bound):
        if c + self.__step < bound:
            return self.__step + 1
        else:
            return bound - c

    def __define_steps(self, coord, pattern_matrix):
        return {
            "i_min": self.__correct_min_step(coord[0]),
            "j_min": self.__correct_min_step(coord[1]),
            "i_max": self.__correct_max_step(coord[0], len(pattern_matrix)),
            "j_max": self.__correct_max_step(coord[1], len(pattern_matrix[0]))
        }

    def __update_matrix(self, next_matrix, pattern_matrix, coord, new_ij_iter):
        steps = self.__define_steps(coord, pattern_matrix)

        next_matrix[coord[0] - steps["i_min"]: coord[0] + steps["i_max"],
                    coord[1] - steps["j_min"]: coord[1] + steps["j_max"]] = \
        pattern_matrix[coord[0] - steps["i_min"]: coord[0] + steps["i_max"],
                       coord[1] - steps["j_min"]: coord[1] + steps["j_max"]]

        i_range = np.arange(coord[0] - steps["i_min"], coord[0] + steps["i_max"])
        j_range = np.arange(coord[1] - steps["j_min"], coord[1] + steps["j_max"])

        ij_range = np.array([list(i_range)*len(j_range),
                             np.repeat(j_range, len(i_range))]).transpose()

        if len(new_ij_iter) > 0:
            new_ij_iter = np.append(new_ij_iter, ij_range, axis=0)
        else:
            new_ij_iter = ij_range
        new_ij_iter = np.unique(new_ij_iter, axis=0)

        """
        for y_step in [0, -1, 1]:
            for x_step in [0, -1, 1]:
                if 0 <= coord[0] + y_step < len(pattern_matrix):
                    if 0 <= coord[1] + x_step < len(pattern_matrix[0]):
                        if [coord[0] + y_step, coord[1] + x_step] not in self.__ij_done:
                            if [coord[0] + y_step, coord[1] + x_step] not in new_ij_iter:
                                next_matrix[coord[0] + y_step][coord[1] + x_step] = pattern_matrix[coord[0] + y_step][coord[1] + x_step]
                                new_ij_iter = new_ij_iter + [[coord[0] + y_step, coord[1] + x_step]]
        """

        return next_matrix, new_ij_iter
