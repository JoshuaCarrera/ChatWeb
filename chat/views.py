from django.shortcuts import render
from .models import Profile, Chat, Message

# Create your views here.
def home(request):
    context = {'available_chats': list(Chat.objects.values())}
    return render(request, 'index.html', context)

def chat_interaction_view(request, id):
    messages = Message.objects.filter(chat=id)
    name_chat = Chat.objects.get(id=id).name
    context = {'messages': messages, 'name_chat': name_chat}
    return render(request, 'chat.html', context)