import logging
import os
import time
import websockets
from aioredis import create_connection, Channel


REDIS_URL = os.getenv("REDIS_CONNECTION", "127.0.0.1")
LOGGER = logging.getLogger(__name__)


async def subscribe_to_redis():
    conn = await create_connection((REDIS_URL, 6379))
    # Set up a subscribe channel
    channel = Channel('test_websocket', is_pattern=False)
    await conn.execute_pubsub('subscribe', channel)
    return channel, conn


async def browser_server(websocket_server):
    """
    The goal of this function is to connect to a Redis channel, wait for messages, and send them using a
    Websockets protocol.
    """
    LOGGER.warning(f"Establishing a connection with the Redis channel test_websocket")
    channel, conn = await subscribe_to_redis()
    uri = f"ws://{websocket_server}:8765"
    LOGGER.warning("Connection established. Waiting for messages to send over websocket protocol.")
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                message = await channel.get()
                LOGGER.warning(f"Sending message {message.decode('utf-8')}")
                await websocket.send(message.decode('utf-8'))
        except websockets.exceptions.ConnectionClosed:
            print('Connection Closed!')
