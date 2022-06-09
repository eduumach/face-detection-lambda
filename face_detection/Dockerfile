FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y python3.8 python3.8-dev python3-pip

COPY app.py requirements.txt haarcascade_frontalface_alt.xml ./

RUN python3.8 -m pip install -r requirements.txt -t .
RUN python3.8 -m pip install awslambdaric

ENTRYPOINT [ "python3.8", "-m", "awslambdaric" ]
CMD [ "app.app" ]

