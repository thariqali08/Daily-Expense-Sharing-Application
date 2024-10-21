from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Expense

class ExpenseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(name="User 1", email="user1@example.com", mobile_number="1234567890")
        self.user2 = User.objects.create(name="User 2", email="user2@example.com", mobile_number="0987654321")

    def test_create_expense(self):
        data = {
            "description": "Dinner",
            "amount": 3000,
            "payer": self.user1.id,
            "participants": [self.user1.id, self.user2.id],
            "split_method": "equal"
        }
        response = self.client.post("/api/expenses/", data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_percentage_split_validation(self):
        data = {
            "description": "Lunch",
            "amount": 4000,
            "payer": self.user1.id,
            "participants": [self.user1.id, self.user2.id],
            "split_method": "percentage",
            "split_details": [
                {"user": self.user1.id, "percentage": 60},
                {"user": self.user2.id, "percentage": 50}
            ]
        }
        response = self.client.post("/api/expenses/", data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Percentages must add up to 100', response.data)
