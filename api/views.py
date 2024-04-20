from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from .models import EventRegistration
from .serializers import EventRegistrationSerializer
from django.shortcuts import get_object_or_404


class IsEventOrganizerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.organizer == request.user or request.user.is_staff


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEventOrganizerOrAdmin]
        return super().get_permissions()


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        event_id = request.data.get('event')
        if event_id is None:
            raise ValidationError("Event ID is required.")

        event = get_object_or_404(Event, pk=event_id)
        if event.organizer == request.user:
            raise ValidationError("Event organizer cannot register for their own event.")

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, event=event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            raise ValidationError("You are already registered for this event.")


class EventSearchAPIView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        events = Event.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
