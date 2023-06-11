import asyncio

from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncConsumer


class MyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket connection", event)
        await self.send(
            {
                "type": 'websocket.accept',
            }
        )

    async def websocket_receive(self, message):
        print("Websocket recived", message)
        for i in range(30):
            await self.send(
                {
                    "type": 'websocket.send',
                    "text": str(i),
                }
            )
            await asyncio.sleep(1)

    async def websocket_disconnect(self, message):
        print("Websocket disconnect", message)
        raise StopConsumer()
