from django.test import TestCase
from rest_framework.test import APIClient
from .models import Booking, MenuItem
from datetime import date, time
from django.contrib.auth.models import User

class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Test",
            email="test@example.com",
            phone="1234567890",
            number_of_guests=2,
            reservation_date=date(2025, 7, 20),
            reservation_time=time(12, 0, 0)
        )
        self.assertEqual(str(booking), 'Test - 2025-07-20 12:00:00')
class MenuItemViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345678')
        MenuItem.objects.create(title="Pizza", price=15.99, inventory=10)
        MenuItem.objects.create(title="Burger", price=10.50, inventory=5)

    def test_get_menu_items(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)