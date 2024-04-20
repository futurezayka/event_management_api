from django.urls import path
from .views import CustomUserRegistrationAPIView, CustomAuthTokenView

urlpatterns = [
    path('register/', CustomUserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', CustomAuthTokenView.as_view(), name='user-login'),
]
