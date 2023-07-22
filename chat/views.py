from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, Messages, Profile

@login_required
def index(request):
    users=User.objects.all().exclude(username=request.user)
    return render(request, "chat/index.html", {"users":users})

@login_required
def room(request, room_name):
    profil=Profile.objects.all().exclude(user=request.user)
    
    users=User.objects.all().exclude(username=request.user)
    room=Room.objects.get(id=room_name)
    messages=Messages.objects.filter(room=room)
    return render(request, "chat/room1.html", {
                                                "room_name": room_name, 
                                                "users":users, 
                                                "room":room,
                                                "messages":messages,
                                                })

def loginForm(request):
    if request.method=="POST":
        
        username=request.POST.get("username")
        password=request.POST.get("password")
        resim=request.POST.get("file")   
        
        user=User.objects.create_user(username=username,password=password)
        profile=Profile.objects.create(user=user, resim=resim)
        profile.save()
        
        if user:
            login(request, user)
            return redirect("index")
            
    return render(request, "chat/login.html")

@login_required
def start_chat(request, username):
    second_user=User.objects.get(username=username)
    try:
        room=Room.objects.get(first_user=request.user, second_user=second_user)
    except Room.DoesNotExist:
        try:
           room=Room.objects.get(second_user=request.user, first_user=second_user)
        except Room.DoesNotExist:
            room=Room.objects.create(first_user=request.user, second_user=second_user)
    return redirect("room", room.id)
    
    
