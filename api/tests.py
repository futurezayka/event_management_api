from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event, EventRegistration
from .models import CustomUser


class EventRegistrationTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpassword')
        self.second_user = CustomUser.objects.create_user(email='seconduser@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_event_registration(self):
        event = Event.objects.create(title='Test Event', description='Test Description', organizer=self.second_user)
        response = self.client.post('/api/event-registration/', {'event': event.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventRegistration.objects.count(), 1)
        self.assertEqual(EventRegistration.objects.get().user, self.user)
        self.assertEqual(EventRegistration.objects.get().event, event)

    def test_create_event_registration_own_event(self):
        event = Event.objects.create(title='Test Event', description='Test Description', organizer=self.user)
        response = self.client.post('/api/event-registration/', {'event': event.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_event_registration_invalid_event_id(self):
        response = self.client.post('/api/event-registration/', {'event': 999}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_event_registration_no_event_id(self):
        response = self.client.post('/api/event-registration/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
