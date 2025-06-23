from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"
        
        user = self.scope["user"]
        if not user or not user.is_authenticated:
            await self.close()
            return
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        print("i got connected nigga")
        
        await self.accept()
        
    async def disconnect(self, close_code):
        print("i got disconnected nigga")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        
        
    async def receive(self, text_data, bytes_data=None):
        data = json.loads(text_data)
        message = data.get("message")
        sender = self.scope["user"].user_name
        
        
        print("i got received nigga")
        
        await self.channel_layer.group_send(
            self.room_group_name,
            
            {
                "type":"chat_message",
                "message":message,
                "sender":sender
            }
        )
        
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender": event["sender"]
        }))
        
        print("i sent a message nigga")
        
        
        
    # def connect(self):
    #     self.accept()
        
    # def disconnect(self, close_code):
    #     pass
    
    
    # def receive(self, text_data=None):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]
        
    #     self.send(text_data=json.dumps({"message":message}))