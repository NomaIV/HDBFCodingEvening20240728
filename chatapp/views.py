from django.shortcuts import render, redirect, get_object_or_404
from .models import User_Profile, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import UserProfileForm, MessageForm
from django.contrib.auth.forms import UserCreationForm

def base_view(request):
    return render(request, 'base.html')

def messages_view(request):
    user_profiles = User_Profile.objects.all()
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'messages.html', 
                  {'user_profile': user_profiles,
                   'messages': messages})

def logout_view(request):
    logout(request)
    return redirect('login_view')

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('massages_view')
        else:
            # Invalid login
            return render(request, 'registration/login.html', {'error': 'Incorrect credentials'})
    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log in the user after signing up
            return redirect('messages_view')
        else:
            return render(request, 'registration/signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form':form})

def user_profile_view(request):
    user = request.user
    profile = get_object_or_404(User_Profile, user=user)

    if request.method =='POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            form.save() # Save user profile
            return redirect('user_profile_view')
        
    else:
        form = UserProfileForm(instance=profile, user=user)
    
    return render(request, 'user_profile.html', {'form': form})





    

