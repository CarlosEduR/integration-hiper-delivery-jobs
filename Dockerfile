FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

ENV TZ=America/Sao_Paulo

RUN groupadd -r app_user && useradd -r -s /bin/false -g app_user app_user && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    apt-get update  && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

RUN chown -R app_user:app_user /app

USER app_user

ENTRYPOINT ["python", "main.py"]