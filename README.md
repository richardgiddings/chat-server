# Chat Server

## Introduction

- A Chat Server using Flask as the server and Redis pubsub to manage messages.
- A Chat Client is available [here](https://github.com/richardgiddings/chat-client).
- Original inspiration came from [here](https://github.com/petronetto/flask-redis-realtime-chat).
- python-decouple is used to manage the config

## Getting Started

It is recommended to use a virtual environment to keep dependencies isolated to just this project.

Install the requirements:
```
pip install -r requirements.txt
``` 

Either add the following environment variables or put them in a .env file:
```
SECRET_KEY - your key
REDIS_HOST - e.g. localhost
REDIS_PORT - e.g. 6379
```

Secret keys can for xample be generated using:
```
openssl rand -hex 32 
```

Run the server using:
```
flask --app server run
```