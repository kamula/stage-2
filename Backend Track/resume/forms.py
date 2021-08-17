from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    email = forms.EmailField(max_length=30)
    class Meta:
        model = Message
        fields = ('email','message')
