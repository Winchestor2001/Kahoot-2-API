from channels.generic.websocket import AsyncWebsocketConsumer


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'room_%s' % room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Process received data
        # You can broadcast the received data to other connected users in the same room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'process_data',
                'data': text_data
            }
        )

    async def process_data(self, event):
        # Send the processed data to the connected user
        await self.send(text_data=event['data'])
