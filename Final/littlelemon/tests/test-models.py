from django.test import TestCase
from restaurant.models import Menu
class menuitemtest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="icecream",price=80,inventory=100)
        self.assertEqual(item,'icecream:80')