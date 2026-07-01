from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Cake", Price=120, Inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu-items/')
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)
