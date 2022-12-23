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
