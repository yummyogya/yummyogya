from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Food
from django.contrib.auth.models import User


class FoodViewTests(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Log the user in

    def test_add_food(self):
        # Prepare the data for a new food item
        food_data = {
            'name': 'Pizza',
            'price': 20,
            'description': 'Delicious cheese pizza',
            'category': 'Fast Food',
            'restaurant': 'Pizza Place'
        }
        
        # Make a POST request to add food
        response = self.client.post(reverse('dashboard:add_food'), food_data)

    # Additional test methods can go here

    def test_edit_food(self):
        # Create a food item for the user
        food = Food.objects.create(
            name='Burger',
            price=15,
            description='Juicy beef burger',
            category='Fast Food',
            restaurant='Burger Joint',
            created_by=self.user  # Associate food item with the logged-in user
        )
        
        # Prepare the updated data for the food item
        updated_food_data = {
            'name': 'Cheeseburger',
            'price': 18,
            'description': 'Juicy beef cheeseburger',
            'category': 'Fast Food',
            'restaurant': 'Burger Joint'
        }
        
        # Make a POST request to edit the food
        response = self.client.post(reverse('dashboard:edit_food', args=[food.pk]), updated_food_data)

