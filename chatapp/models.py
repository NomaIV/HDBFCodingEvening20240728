from django.db import models
from django.contrib.auth.models import User
# Three models needed, message, online_users and user_profile

# Message Model
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    images = models.ImageField(upload_to='images', blank=True, null=True)
    videos = models.FileField(upload_to='videos',blank=True, null=True, max_length=100)
    voice_notes = models.FileField(upload_to='voice_notes', blank=True, null=True, max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    delete_message = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User,related_name ='deleted_messages', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
# Online User
class Online_Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.timestamp)
    
# User Profile 
class User_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    online = models.BooleanField(default=False)
    status = models.TextField()
    last_seen = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True,null=True)

    def __str__(self):
        return str(self.user)
    



