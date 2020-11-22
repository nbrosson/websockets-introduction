import asyncio
import logging
from aioredis import create_connection, Channel
import websockets
import os


LOGGER = logging.getLogger(__name__)


async def server(websocket, path):
    LOGGER.warning("Server starting")
    try:
        while True:
            message = await websocket.recv()
            # Feed this data to the PUBLISH co-routine
            LOGGER.warning("New message received")
            LOGGER.warning(message)

            await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosed:
        print('Connection Closed!')