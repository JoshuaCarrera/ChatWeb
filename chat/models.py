from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_pics', null=True)
    def __str__(self):
        return f'{self.user.username} Profile'

class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='messages_sent', on_delete=models.SET_NULL, null=True)
    to_user = models.ForeignKey(User, related_name='messages_received', on_delete=models.SET_NULL, null=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    file = models.FileField(upload_to=None, max_length=100)
    def __str__(self):
        return f'{self.data_sent} | from {self.from_user.username} to {self.to_user.username}'
    