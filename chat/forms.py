
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['name', 'description', 'users']
    
    def __init__(self, user_profile_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['users'].queryset = self.fields['users'].queryset.exclude(id=user_profile_id)