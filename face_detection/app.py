
from flask import request
from flask_lambda import FlaskLambda
import base64
import numpy as np
import cv2

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

    image = base64.b64decode(file)
    file_bytes = np.asarray(bytearray(image), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.08,
        minNeighbors=4,
        minSize=(45, 90),
        maxSize=(250, 650)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    image = cv2.imencode('.jpg', img)[1]
    return {"image": str(base64.b64encode(image).decode('utf-8', 'strict'))}
