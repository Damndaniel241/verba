from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions,status
from .models import ChatRoom,NewUser
from .serializers import ChatRoomSerializer
# Create your views here.



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_room_id(request, format=None):
    try:
        recipient = request.data.get("recipient_id")
        sender = request.user
        
        if not recipient:
            return Response({"error": "Recipient ID required."}, status=400)

        recipient = NewUser.objects.get(id=recipient)

        # Ensure consistent ordering to avoid duplicates
        user1, user2 = sorted([sender, recipient], key=lambda u: u.pk)

        room, created = ChatRoom.objects.get_or_create(user1=user1, user2=user2)
        serializer = ChatRoomSerializer(room)
        return Response({"message":"room id successful", "data":serializer.data},status=status.HTTP_200_OK)
    except NewUser.DoesNotExist:
        return Response({"error": "Recipient not found"}, status=404)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)