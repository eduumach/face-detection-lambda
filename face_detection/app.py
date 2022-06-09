
from flask import request
from flask_lambda import FlaskLambda
import base64
import numpy as np
import cv2
import utils

app = FlaskLambda(__name__)


@app.route("/process-image", methods=["POST"])
def process_image():
    img = request.json["image"]

    header = {
        'Content-Type': 'application/json',
    }

    body = face_detect(img)

    return body, 200, header


def face_detect(file):

    image = utils.decode(file)

    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.08,
        minNeighbors=4,
        minSize=(45, 90),
        maxSize=(250, 650)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    image_base64 = utils.encode(image)
    return {"image": image_base64}
