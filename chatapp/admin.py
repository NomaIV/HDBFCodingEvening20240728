from django.contrib import admin
from django.contrib.auth.models import User
from .models import User_Profile, Message,Online_Users

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display =('user', 'text', 'timestamp', 'delete_message')
    search_fields =('text', 'user__username') # Can search by
    list_filter = ('timestamp', 'delete_message') # Can filter by
    
@admin.register(Online_Users)
class Online_UsersAdmin(admin.ModelAdmin):
    list_display =('user','timestamp')
    search_fields =('user__username',)
    list_filter =('timestamp',)

@admin.register(User_Profile)
class User_ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'online', 'status', 'last_seen')
    search_fields =('user__username', 'status')
    list_filter =('online', 'last_seen')
    

    

