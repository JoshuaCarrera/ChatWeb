from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile, Chat, Message
from .forms import MessageForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def chat_list(request):
    user_profile = Profile.objects.get(user=request.user.id)
    available_chats = Chat.objects.filter(users=user_profile)
    context = {'available_chats': available_chats}
    return render(request, 'chat_list.html', context)

def profile_view(request, id):
    profile = Profile.objects.get(id=id)
    messages_sents = Message.objects.filter(sender_id=id)
    context = {'profile': profile, 'messages_sents': messages_sents}
    return render(request, 'profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            profile = Profile.objects.create(user=user)
            user.save()
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm
    
    context = {'form': form}
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'signin.html', {"form": AuthenticationForm})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def chat_interaction_view(request, id):
    messages = Message.objects.filter(chat=id)
    current_chat = Chat.objects.get(id=id)
    context = {'messages': messages, 'chat': current_chat}
    return render(request, 'chat.html', context)
