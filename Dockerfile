FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y \
      libraqm-dev \
      python3 \
      python3-arrow \
      python3-icalendar \
      python3-pil \
      python3-yaml \
      python3-requests \
      python3-recurring-ical-events \
      zlib1g-dev \
      libjpeg-dev \
      wget unzip \
      libfreetype6-dev \
      fonts-firacode \
      fonts-roboto-hinted && \
    cd /opt && wget https://use.fontawesome.com/releases/v6.5.2/fontawesome-free-6.5.2-desktop.zip && \
    unzip *.zip && ls && rm *.zip && \
    apt-get clean

CMD ["/bin/bash"]
