import json
from PIL import Image


class FileTools(object):

    @staticmethod
    def read_json(file_path):
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def read_image(file_path):
        return Image.open(file_path)
