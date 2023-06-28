from django.shortcuts import render
from .models import Profile, Chat, Message

# Create your views here.
def home(request):
    context = {'available_chats': list(Chat.objects.values())}
    return render(request, 'index.html', context)