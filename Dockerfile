
FROM python:3.8-slim-buster

WORKDIR .
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV FLASK_APP="app"

COPY . .

EXPOSE 5001
CMD ["python3", "runner.py"]