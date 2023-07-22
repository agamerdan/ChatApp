from django.db import models
from django.contrib.auth.models import User
import uuid

class Room(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_user=models.ForeignKey(User,related_name="room_first",on_delete=models.CASCADE, null=True)
    second_user=models.ForeignKey(User,related_name="second_first",on_delete=models.CASCADE, null=True)
    
class Messages(models.Model):
    user=models.ForeignKey(User,related_name="messages", verbose_name="Kullanıcı",on_delete=models.CASCADE)
    room=models.ForeignKey(Room, related_name="messages",verbose_name="Oda",on_delete=models.CASCADE)
    content=models.TextField(verbose_name="Mesaj içeriği")
    created_date=models.DateTimeField(auto_now_add=True)
    WhatisType=models.CharField(max_length=50,null=True)
    
    def get_short_date(self):
        return str(self.created_date.hour) +":"+ str(self.created_date.minute)
    
class Profile (models.Model):
    def default_image():
        # Varsayılan resmin yolunu belirtin. Projenize uygun bir yol vermelisiniz.
       return 'media/avatar.png'
    
    user=models.OneToOneField(User, related_name="userProfil",on_delete=models.CASCADE)
    resim=models.FileField(default='media/avatar.png')
    
    


