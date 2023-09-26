FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y git && \
    apt-get install -y python3-pip


WORKDIR /src
RUN pip install pyyaml
RUN pip install autobahn


