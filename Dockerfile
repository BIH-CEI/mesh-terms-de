FROM python:3.10

LABEL org.opencontainers.image.source="https://github.com/BIH-CEI/mesh-terms-de"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY mesh_terms/ mesh_terms
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]