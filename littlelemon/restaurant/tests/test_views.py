from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    """
    Test case for the MenuView API endpoint.
    """
    def setUp(self):
        """
        Set up the test data for the MenuView.
        Creates a few MenuItem instances to be used in the tests.
        """
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(
            title="Pizza", 
            price=15.99, 
            inventory=10
        )
        self.item2 = MenuItem.objects.create(
            title="Pasta", 
            price=12.50, 
            inventory=20
        )
        self.item3 = MenuItem.objects.create(
            title="Salad", 
            price=8.75, 
            inventory=15
        )

    def test_getall(self):
        """
        Test to retrieve all menu items and verify the serialized data.
        """
        # Get the list of menu items from the database
        menu_items = MenuItem.objects.all()
        # Serialize the data using the MenuItemSerializer
        serialized_data = MenuItemSerializer(menu_items, many=True).data
        
        # Make a GET request to the menu endpoint
        response = self.client.get('/restaurant/menu/')

        # Check if the response status code is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the data returned in the response matches the serialized data
        self.assertEqual(response.data, serialized_data)

 