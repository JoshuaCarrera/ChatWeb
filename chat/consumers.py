import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Message, Chat


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat = Chat.objects.get(id=self.chat_id)

        self.user = self.scope['user']
        self.profile = self.user.profile

        self.room_group_name = f'chat_{self.chat_id}'

        print("You connect to " + self.room_group_name, self.user)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_sender = text_data_json['sender']

        # Guardar el mensaje en la base de datos
        self.save_message(self.profile, self.chat, message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'sender': message_sender
            }
        )

    def save_message(self, sender, chat, text):
        message = Message.objects.create(sender=sender, chat=chat, text=text)
        message.save()

    def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'sender': sender,
            'profile_name': self.profile.user.username,
            'profile_pic': self.profile.img.url,
        }))