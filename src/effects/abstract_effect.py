from src.creators.image import Img


class AbstractEffect(object):

    def __init__(self):
        self._main_value = 1
        self._least_value = 0

    def apply_on(self, base_image):
        raise NotImplementedError

    @staticmethod
    def _to_image(matrix, colors):
        return Img(matrix, colors)

    def _compute_background(self, base_image):
        row = list()
        for j in range(0, len(base_image["image"][0])):
            row.append(self._least_value)

        matrix = list()
        for i in range(0, len(base_image["image"])):
            matrix.append(row.copy())

        return matrix
