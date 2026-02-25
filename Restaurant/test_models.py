from django.test import TestCase
from .models import Booking, Menu

class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            bookingdate="2024-07-01 19:00:00"
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.number_of_guests, 4)
        self.assertEqual(str(self.booking), "John Doe - 2024-07-01 19:00")
        
class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pasta",
            price=12.99,
            inventory=10
        )

    def test_menu_creation(self):
        self.assertEqual(self.menu_item.title, "Pasta")
        self.assertEqual(self.menu_item.price, 12.99)
        self.assertEqual(self.menu_item.inventory, 10)
        self.assertEqual(str(self.menu_item), "Pasta - $12.99") 