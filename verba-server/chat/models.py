from django.db import models
from user.models import NewUser
import uuid
# Create your models here.
   

class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(NewUser,null=True, related_name="chatrooms_initiated", on_delete=models.CASCADE)
    user2 = models.ForeignKey(NewUser,null=True, related_name="chatrooms_received", on_delete=models.CASCADE)
    # is_group = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user1", "user2"], name="unique_user_pair"),
        ]
   
   
    def __str__(self):
        return f"room id is {id}"

class Message(models.Model):
    room_id = models.ForeignKey(ChatRoom,on_delete=models.CASCADE, null=True)
    sender_id = models.ForeignKey(NewUser,null=True,on_delete=models.SET_NULL,related_name='sent_messages')
    # participants = models.ManyToManyField(NewUser, related_name="chat_rooms")
    # recipient_id = models.ForeignKey(NewUser,null=True,on_delete=models.SET_NULL,related_name='received_messages')
    content = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.sender_id}'s message"