FROM python:3.8-slim-buster

WORKDIR .
# Update default packages
RUN apt-get update

# Get Ubuntu packages
RUN apt-get install -y \
    build-essential \
    curl

RUN apt-get install ffmpeg libsm6 libxext6  -y
# Update new packages
RUN apt-get update

# Get Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV FLASK_APP="app"

COPY . .

EXPOSE 5001
CMD ["python3", "runner.py"]