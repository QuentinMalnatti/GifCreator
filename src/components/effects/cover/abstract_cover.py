# Internal libs
from components.effects.abstract_effect import AbstractEffect

# External libs
import copy
import numpy as np


class AbstractCover(AbstractEffect):

    def __init__(self):
        super().__init__()
        self._step = 2
        self.__ij_done = None

    def _init(self, pattern):
        self.__ij_done = self.matrix_tools.compute_1value_matrix(pattern["pattern"])
        return {"ij_iter": self._get_first_pixel(pattern["pattern"])}

    def _compute_first_image(self, pattern):
        matrix = pattern["image"]
        coord_0 = self._get_first_pixel(matrix)
        matrix[coord_0[0], coord_0[1]] = pattern["image_binary"][coord_0[0], coord_0[1]]
        self.__ij_done[coord_0[0], coord_0[1]] += 1
        return matrix

    def _get_first_pixel(self, matrix):
        raise NotImplementedError

    def _is_finish(self):
        return len(self.__ij_done[self.__ij_done == 0]) == 0

    def _compute_next_image(self, current_matrix, pattern, iter_components):
        ij_iter = iter_components["ij_iter"]
        next_matrix = copy.deepcopy(current_matrix)

        i_iter, j_iter = ij_iter[0], ij_iter[1]

        new_i, new_j = np.array([], dtype=int), np.array([], dtype=int)
        step_range = np.arange(-self._step, self._step + 1)
        for i_step in step_range:
            for j_step in step_range:
                if self._is_good_step([i_step, j_step]):
                    new_i = np.append(new_i, i_iter + i_step)
                    new_j = np.append(new_j, j_iter + j_step)

        cond_i = ((new_i >= 0) & (new_i < len(next_matrix)))
        cond_j = ((new_j >= 0) & (new_j < len(next_matrix[0])))
        new_i = new_i[cond_i & cond_j]
        new_j = new_j[cond_i & cond_j]

        self.__ij_done[self.__ij_done > 0] += 1
        self.__ij_done[new_i, new_j] += 1  # cells with value 1 are new ones

        next_ij = np.where(self.__ij_done == 1)
        next_ij = np.array([next_ij[0], next_ij[1]])
        next_matrix[next_ij[0], next_ij[1]] = pattern["image_binary"][next_ij[0], next_ij[1]]

        return next_matrix, {"ij_iter": next_ij}

    def _is_good_step(self, step):
        raise NotImplementedError
