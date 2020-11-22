# What is Websockets?

WebSocket is a computer communications protocol, providing full-duplex communication channels over a single 
TCP connection. WebSocket is distinct from HTTP, even though both protocols are located at layer 5 in the OSI model 
and depend on TCP at layer 4. WebSocket "is designed to work over HTTP ports 443 and 80 as 
well as to support HTTP proxies and intermediaries," thus making it compatible with the HTTP protocol. 
To achieve compatibility, the WebSocket handshake uses the HTTP Upgrade header to change from the HTTP protocol 
to the WebSocket protocol.

**Why it is useful?** Because an HTTP request needs to wait for a server response, while Websocket protocol allows 
the client to directly reach the server without waiting any responses. 


# The project

The goal of this project is to provide a simple setup for a websockets implementation in Python. The architecture is 
the following: Whenever a Redis message is published in the right channel (here, test_websocket), a Websockets
Publisher will receive it and send it to a Websockets Consumer.

The main.py file is responsible for managing the Python commands. Then, consumer.py is the Websocket consumer, while 
publisher.py is the Websocket publisher.  

# How to start the program

## Build a virtual environment and install dependencies (Windows)

python -m venv .venv
C:\Users\...\.venv\Scripts\activate.bat

pip install -r requirements.txt

## Setup a redis environment (You can also use a Redis Docker container)

- Install Redis
- Start a Redis server (see Redis documentation)


## Run a websocket server

Open two terminals with the python environment you created. Run the following commands (the order must be respected
):

```
Terminal 1: python main.py start-consumer "localhost"
Terminal 2: python main.py start-publisher "localhost"
```

## Now, publish messages from Redis

```
// First terminal
PUBLISH test_websocket hello
PUBLISH test_websocket Check 
PUBLISH test_websocket Your
PUBLISH test_websocket Python
PUBLISH test_websocket Consumer
PUBLISH test_websocket Outputs
```
