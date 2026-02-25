from django.test import TestCase
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet
from .models import Menu, Booking

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
class MenuItemViewTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pasta",
            price=12.99,
            inventory=10
        )

    def test_menu_item_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pasta")
        
class SingleMenuItemViewTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pasta",
            price=12.99,
            inventory=10
        )

    def test_single_menu_item_view(self):
        response = self.client.get(f'/menu/{self.menu_item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pasta")  

class BookingViewSetTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            bookingdate="2024-07-01 19:00:00"
        )

    def test_booking_view_set(self):
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")   
        
class BookingViewSetDetailTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            bookingdate="2024-07-01 19:00:00"
        )

    def test_booking_view_set_detail(self):
        response = self.client.get(f'/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")            