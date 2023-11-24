# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Set up Python environment and install dependencies
RUN python -m venv .venv

# Ative o ambiente virtual e instale as dependências
SHELL ["bash", "-c"]
RUN source .venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for Flask (assumindo que seu aplicativo Flask é chamado app.py)
ENV FLASK_APP=app.py

# Comando para iniciar o aplicativo Flask
CMD ["bash", "-c", "source .venv/bin/activate && flask run -h 0.0.0.0 -p 5000"]