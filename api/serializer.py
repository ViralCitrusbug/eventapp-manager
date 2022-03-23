from rest_framework import serializers
from . models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
    
    def update(self, instance, validated_data):
        print("**************")
        new_event = Event(**validated_data)
        new_event.id = instance.id
        new_event.save()
        print("***************")
        return new_event
    

class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields ="__all__"
    
    def create(self, validated_data):
        print(validated_data)
        event =  EventDate.objects.create(**validated_data)
        print(event)
    
class EventSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSlot
        fields = "__all__"

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"