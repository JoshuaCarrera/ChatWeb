from django.shortcuts import render
from .models import Profile, Chat, Message
from .forms import MessageForm

# Create your views here.
def home(request):
    context = {'available_chats': list(Chat.objects.values())}
    return render(request, 'index.html', context)

def profile_view(request, id):
    profile = Profile.objects.get(id=id)
    messages_sents = Message.objects.filter(sender_id=id)
    context = {'profile': profile, 'messages_sents': messages_sents}
    return render(request, 'profile.html', context)

def chat_interaction_view(request, id):
    messages = Message.objects.filter(chat=id)
    current_chat = Chat.objects.get(id=id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = current_chat
            message.sender = request.user.profile
            message.save()
            form = MessageForm()
    else:
        form = MessageForm()

    context = {'messages': messages, 'chat': current_chat, 'form': form}
    return render(request, 'chat.html', context)

def message_send(request):
    pass



