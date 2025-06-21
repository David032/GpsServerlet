# REMEMBER: needs to be ran privieged 
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 5002

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#GCC, build tools & i2c checking
RUN apt-get update && apt-get install -y gcc 
RUN apt-get install build-essential -y

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

#check i2c

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
RUN adduser appuser i2c
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]
