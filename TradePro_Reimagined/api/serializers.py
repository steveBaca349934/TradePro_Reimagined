from rest_framework import serializers
from .models import Room

#A serializer transforms a table in our database into a JSON response
#That the front end can utilize
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause',\
            'votes_to_skip','created_at')

        

