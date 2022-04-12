FROM debian:buster

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y \
      libraqm-dev \
      python3 python3-pip \
      fonts-firacode \
      vim \
      fonts-font-awesome \
      fonts-roboto-hinted \
      zlib1g-dev \
      libjpeg-dev \
      libfreetype6-dev \
      fonts-fork-awesome \
      unzip \
      wget && \
    pip3 install -r requirements.txt && \
    cd /opt && wget https://github.com/FortAwesome/Font-Awesome/releases/download/5.15.2/fontawesome-free-5.15.2-desktop.zip && \
    unzip *.zip && ls && rm *.zip && \
    apt-get clean

CMD ["/bin/bash"]
