from django import forms
from django.db.models.base import Model
from .models import User_Profile, Message

# Message
class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ['text', 'images', 'videos', 'voice_notes']
        widgets = {'text': forms.Textarea(attrs={'rows': 2})}

# User Profile
class UserProfileForm(forms.ModelForm):
    # Add username field to the form
    username = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User_Profile
        fields = ['status', 'profile_pic'] # Can edit
        widgets = {'status': forms.Textarea(attrs={'rows': 2})}

    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user') # Extract the user from kwargs
        super().__init__(*args,**kwargs)
        self.fields['username'].initial = user.username # Set the initial value for username

    def save(self, commit =True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user