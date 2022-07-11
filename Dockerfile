FROM python:3.11-rc-slim-bullseye
FROM gorialis/discord.py 

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN pip install -r ./deployment/requirements.txt

RUN bash ./deployment/entrypoint.sh

ENTRYPOINT [ "python3", "main.py" ]