# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Install uvicorn
RUN pip install uvicorn

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "api.serve:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]