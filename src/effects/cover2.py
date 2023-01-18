# Internal libs
from src.effects.abstract_effect import AbstractEffect

# External libs
import copy
from datetime import datetime


class Cover2(AbstractEffect):

    def __init__(self):
        super().__init__()
        self.__ij_done = []

    @staticmethod
    def __get_first_pixel():
        return [0, 0]

    def apply_on(self, pattern):
        self.__ij_done.append(self.__get_first_pixel())
        matrix = self.__compute_first_image(pattern)
        list_img = [self._to_image(copy.deepcopy(matrix), pattern["colors"]).content]

        ij_iter = [self.__get_first_pixel()]
        while (len(self.__ij_done) < len(pattern["pattern"])*len(pattern["pattern"][0])): # and self._cpt < 35:
            print("compute next matrix")
            s = datetime.now()
            matrix, ij_iter = self.__compute_next_image(matrix, pattern["pattern"], ij_iter)
            print(datetime.now() - s)
            print("append image")
            s = datetime.now()
            list_img.append(self._to_image(copy.deepcopy(matrix), pattern["colors"]).content)
            print(datetime.now() - s)
            self._cpt += 1
        print(f"{self._cpt} iterations")
        return list_img

    def __compute_first_image(self, pattern):
        matrix = self._compute_background(pattern)
        matrix[self.__ij_done[0][0]][self.__ij_done[0][1]] = pattern["pattern"][self.__ij_done[0][0]][self.__ij_done[0][1]]
        return matrix

    def __compute_next_image(self, current_matrix, pattern_matrix, ij_iter):
        next_matrix = copy.deepcopy(current_matrix)
        new_ij_iter = []
        for coord in ij_iter:
            next_matrix, new_ij_iter = self.__update_matrix(next_matrix, pattern_matrix, coord, new_ij_iter)
        return next_matrix, new_ij_iter

    def __update_matrix(self, next_matrix, pattern_matrix, coord, new_ij_iter):
        for y_step in [0, -1, 1]:
            for x_step in [0, -1, 1]:
                if 0 <= coord[0] + y_step < len(pattern_matrix):
                    if 0 <= coord[1] + x_step < len(pattern_matrix[0]):
                        next_matrix[coord[0] + y_step][coord[1] + x_step] = pattern_matrix[coord[0] + y_step][coord[1] + x_step]
                        if [coord[0] + y_step, coord[1] + x_step] not in self.__ij_done:
                            self.__ij_done.append([coord[0] + y_step, coord[1] + x_step])
                            new_ij_iter.append([coord[0] + y_step, coord[1] + x_step])
        return next_matrix, new_ij_iter

