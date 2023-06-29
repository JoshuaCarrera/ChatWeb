from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path((''), views.home, name='home'),
    path(('signup/'), views.signup, name='signup'),
    path(('signin/'), views.signin, name='signin'),
    path(('signout/'), views.signout, name='signout'),    
    path(('chat/<int:id>'), views.chat_interaction_view, name='chat_interaction_view'),
    path(('profile/<int:id>'), views.profile_view, name='profile_view'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para poder servir archivos
