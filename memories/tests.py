from django.contrib.auth.models import User
from django.test import TestCase

from .models import Memory


class MemoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        Memory.objects.create(
            user=self.user,
            comments="This is a test memory.",
            place_name="Test Location",
            latitude=10.823100,
            longitude=106.62970,
        )

    def test_memory_creation(self):
        memory = Memory.objects.filter(place_name="Test Location").first()
        self.assertEqual(memory.comments, "This is a test memory.")
        self.assertAlmostEqual(float(memory.latitude), 10.823100, places=6)
        self.assertAlmostEqual(float(memory.longitude), 106.62970, places=5)

    def test_memory_list(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Location")
