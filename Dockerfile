FROM jenkins/jenkins:lts

USER root

# Установка Python и необходимых утилит
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Создание виртуального окружения Python (опционально, но полезно)
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Установка Python-библиотек
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# Создание рабочей директории
RUN mkdir -p /home/jenkins

# Копирование всех необходимых скриптов внутрь контейнера
COPY download.py train_model.py jenkins_pipeline.sh /home/jenkins/

# Даем права на выполнение shell-скрипта
RUN chmod +x /home/jenkins/jenkins_pipeline.sh

# Переключаемся на пользователя Jenkins
USER jenkins

# Назначаем рабочую директорию по умолчанию
WORKDIR /home/jenkins
