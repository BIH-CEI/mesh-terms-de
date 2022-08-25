ARG BASE=python:3.10-alpine


FROM $BASE

LABEL org.opencontainers.image.source="https://github.com/BIH-CEI/mesh-terms-de"

WORKDIR /app

COPY requirements.txt .
RUN apk add --virtual build-dependencies build-base \
    && pip install $(grep "pandas" requirements.txt) \
    && apk del build-dependencies
RUN apk add --no-cache libstdc++

RUN pip install -r requirements.txt

COPY mesh_terms/ mesh_terms
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]