from django.test import TestCase
from users.models import CustomUser


class CustomUserManagerTestCase(TestCase):
    def test_create_user(self):
        """Test creating a new user"""
        email = 'test@example.com'
        password = 'testpassword'
        user = CustomUser.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        email = 'admin@example.com'
        password = 'adminpassword'
        superuser = CustomUser.objects.create_superuser(email=email, password=password)

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
