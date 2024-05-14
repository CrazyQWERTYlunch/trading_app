"""
Module for connecting to the chat WebSocket endpoint and logging messages.

This module establishes a WebSocket connection to the chat server, listens for incoming messages,
and logs them into a text file.

"""
import aiohttp
import time
import asyncio

async def main():
    """
    Establishes a WebSocket connection to the chat server and logs incoming messages.

    This function connects to the chat WebSocket endpoint, listens for incoming messages,
    and logs each message into a text file named "ws_messages.txt".

    Raises:
        aiohttp.ClientError: If there is an error during the WebSocket connection.
    """
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time() * 1000)
        async with session.ws_connect(f'http://localhost:8000/chat/ws/{client_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")

asyncio.run(main())
