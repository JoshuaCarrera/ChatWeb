from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='chat/profile_pics/', default='chat/profile_pics/default_profile_logo.png', blank=True)
    def __str__(self):
        return f'{self.user.username}'

class Chat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(Profile, related_name='chats')
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='messages_sents', on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE, default=None)
    date_sent = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    file = models.FileField(upload_to='chat/chat_files', blank=True, default=None)

    class Meta:
        ordering = ('date_sent',)

    def __str__(self):
        return f'{self.date_sent} | from {self.sender.user.username} to {self.chat.name}'
    