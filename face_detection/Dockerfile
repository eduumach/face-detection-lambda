FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y python3.8 python3.8-dev python3-pip

COPY app.py requirements.txt haarcascade_frontalface_alt.xml ./

RUN python3.8 -m pip install -r requirements.txt -t .
RUN python3.8 -m pip install awslambdaric

ENTRYPOINT [ "python3.8", "-m", "awslambdaric" ]
CMD [ "app.app" ]






#
#
#RUN python3.8 -m pip install -r requirements.txt -t .
#
##ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
##RUN chmod 755 /usr/bin/aws-lambda-rie
##COPY a.sh ./
##RUN chmod +x a.sh
#
##ENTRYPOINT [ "./a.sh" ]
##CMD [ "wsgi_handler.handler" ]
#CMD ["app.app"]