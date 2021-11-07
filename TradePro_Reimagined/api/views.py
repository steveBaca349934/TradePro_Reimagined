from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response 


# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer


    def post(self, request, format = None):

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()


        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            #pieces of information necessary to create a new room...
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key

            #query our Room table from our sqllite database
            queryset = Room.objects.filter(host = host)
            #if the room we are about to initialize already exists then 
            #we just want to set the room equal to the existing room...
            if queryset.exists():

                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields = ['guest_can_pause','votes_to_skip'])

            else:
                #if it doesn't exist then we can go ahead and create a new room ...
                room = Room(host = host, guest_can_pause = guest_can_pause, votes_to_skip = votes_to_skip)
                room.save()

            #returns json formatted data and a status code
            return Response(RoomSerializer(room).data, status = status.HTTP_200_OK)



