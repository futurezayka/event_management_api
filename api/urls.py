from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventRegistrationViewSet, EventSearchAPIView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'event-registration', EventRegistrationViewSet, basename='event-registration')

urlpatterns = [
    *router.urls,
]

urlpatterns += [
    path('events/<int:pk>/', EventViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='event-detail'),
    path('events/search', EventSearchAPIView.as_view(), name='event_search'),
]
