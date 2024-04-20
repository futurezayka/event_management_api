from rest_framework import serializers
from .models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer']
        read_only_fields = ['organizer']

    def validate(self, attrs):
        request = self.context.get('request')
        if self.instance and self.instance.organizer != request.user:
            raise serializers.ValidationError("Only event organizer can edit or delete this event.")
        return attrs


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['id', 'user', 'event', 'registration_date']
        read_only_fields = ['registration_date', 'event']
        extra_kwargs = {
            'user': {'required': False}
        }

    def validate(self, attrs):
        request = self.context.get('request')
        if 'event' in attrs:
            event = attrs['event']
            if event.organizer == request.user:
                raise serializers.ValidationError("Event organizer cannot register for their own event.")
        return attrs
