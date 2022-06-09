import base64

import cv2
import numpy as np


def decode(file):
    image = base64.b64decode(file)
    file_bytes = np.asarray(bytearray(image), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return image


def encode(image):
    image = cv2.imencode('.jpg', image)[1]
    return str(base64.b64encode(image).decode('utf-8', 'strict'))