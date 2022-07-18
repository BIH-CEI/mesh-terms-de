FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY mesh_terms/ mesh_terms
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]