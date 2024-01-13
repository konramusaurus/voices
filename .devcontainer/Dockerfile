FROM python:3.12.1-bookworm

ARG USERNAME=dev
RUN useradd -m -d /home/$USERNAME -s /bin/bash $USERNAME\
    && apt update \
    && apt install -y sudo curl gcc git\
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN pip install -U pip && pip install poetry
