import numpy as np


class ImageTools(object):

    @staticmethod
    def image_to_pattern(image):
        pattern = {
            "image": None,
            "image_binary": None,
            "pattern": None,
            "colors": {
                "0": [0, 0, 0],
                "1": [255, 255, 255]
            }
        }

        image = image.convert("RGB")
        pattern["image"] = np.array(image)

        image = image.convert('L')
        image = image.point(lambda p: 255 if p > 255/2 else 0)
        pattern["pattern"] = np.array(image.point(lambda p: 1 if p > 255/2 else 0))

        image = image.convert("RGB")
        pattern["image_binary"] = np.array(image)

        return pattern
