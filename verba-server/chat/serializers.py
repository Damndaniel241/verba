from rest_framework import serializers
from .models import ChatRoom,Message
from user.serializers import NewUserSerializer

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"
        
        
class MessageSerializer(serializers.ModelSerializer):
    sender_id = NewUserSerializer()
    class Meta:
        model = Message
        fields = ["id","room_id","content","sender_id","timestamp"]