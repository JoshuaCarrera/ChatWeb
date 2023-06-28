from django.urls import path
from . import views

urlpatterns = [
    path((''), views.home, name='home'),
    path(('chat/<int:id>'), views.chat_interaction_view, name='chat_interaction_view')
]