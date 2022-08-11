FROM python:3.11-rc-slim-bullseye
FROM gorialis/discord.py 

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN pip install -r ./deployment/requirements.txt


ENTRYPOINT [ "python3", "main.py" ]