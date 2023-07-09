import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async

from .models import Message, Chat, Profile


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.user = self.scope['user']
        self.room_group_name = f'chat_{self.chat_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        await self.close()


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']

        await self.save_message(sender, self.chat_id, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'sender': sender
            }
        )

    @sync_to_async
    def save_message(self, sender, chat_id, text):
        sender = Profile.objects.get(id=sender)
        chat = Chat.objects.get(id=chat_id)
        Message.objects.create(sender=sender, chat=chat, text=text)

    @sync_to_async
    def get_user_profile(self):
        return self.user.profile

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        profile = await self.get_user_profile()

        await self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'sender': sender,
            'profile_name': self.user.username,
            'profile_pic': profile.img.url,
        }))