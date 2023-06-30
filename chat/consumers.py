import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        chat_id = self.scope['url_route']['kwargs']['chat_id']
        user = self.scope['user']

        self.profile_name = user.username
        self.profile_pic = user.profile.img.url

        self.room_group_name = f'chat_{chat_id}'

        print("You connect to " + self.room_group_name, self.profile_pic, self.profile_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_sender = text_data_json['sender']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'sender': message_sender
            }
        )

    def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'sender': sender,
            'profile_name': self.profile_name,
            'profile_pic': self.profile_pic,
        }))