import click
import logging
import asyncio
import websockets
import functools
from src.publisher import browser_server
import time
from src.consumer import server

LOGGER = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('websocket_server')
def start_publisher(websocket_server):
    """
    Publish messages through websocket

    :params websocket_server: The ip address of the server to which messages must be sent

    """
    asyncio.get_event_loop().run_until_complete(browser_server(websocket_server))


@cli.command()
@click.argument('websocket_server')
def start_consumer(websocket_server):
    """
    Listen to every new messages and print them

    :params websocket_server: The ip address of the consumer (the server that receives messages)

    """
    start_server = websockets.serve(server, websocket_server, 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    cli()
