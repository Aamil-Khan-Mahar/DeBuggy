import unittest
from unittest.mock import MagicMock
from Code5Correct.py import Backend  

class TestBackend(unittest.TestCase):
    def setUp(self):
        # Mock database
        self.mock_database = {}
        self.backend = Backend(self.mock_database)

    def test_create_user(self):
        self.backend.create_user("user1", {"password": "pass123", "profile": {}, "active": True})
        self.assertIn("user1", self.mock_database)

        with self.assertRaises(ValueError):
            self.backend.create_user("user1", {"password": "pass123"})

    def test_get_user(self):
        self.backend.create_user("user1", {"password": "pass123"})
        user = self.backend.get_user("user1")
        self.assertEqual(user["password"], "pass123")

    def test_update_user(self):
        self.backend.create_user("user1", {"password": "pass123"})
        self.backend.update_user("user1", {"password": "newpass"})
        user = self.backend.get_user("user1")
        self.assertEqual(user["password"], "newpass")

        with self.assertRaises(ValueError):
            self.backend.update_user("user2", {"password": "pass123"})

    def test_delete_user(self):
        self.backend.create_user("user1", {"password": "pass123"})
        self.backend.delete_user("user1")
        self.assertNotIn("user1", self.mock_database)

        with self.assertRaises(ValueError):
            self.backend.delete_user("user1")

    def test_list_users(self):
        self.backend.create_user("user1", {"password": "pass123"})
        self.backend.create_user("user2", {"password": "pass456"})
        self.assertEqual(set(self.backend.list_users()), {"user1", "user2"})

    def test_authenticate_user(self):
        self.backend.create_user("user1", {"password": "pass123"})
        self.assertTrue(self.backend.authenticate_user("user1", "pass123"))
        self.assertFalse(self.backend.authenticate_user("user1", "wrongpass"))
        self.assertFalse(self.backend.authenticate_user("user2", "pass123"))

    def test_change_password(self):
        self.backend.create_user("user1", {"password": "pass123"})
        self.backend.change_password("user1", "pass123", "newpass")
        self.assertTrue(self.backend.authenticate_user("user1", "newpass"))

        with self.assertRaises(ValueError):
            self.backend.change_password("user1", "wrongpass", "newpass")

    def test_search_users(self):
        self.backend.create_user("user1", {"password": "pass123", "profile": {"name": "Alice"}})
        self.backend.create_user("user2", {"password": "pass456", "profile": {"name": "Bob"}})
        results = self.backend.search_users("Alice")
        self.assertIn("user1", results)
        self.assertNotIn("user2", results)

    def test_user_profile(self):
        self.backend.create_user("user1", {"password": "pass123", "profile": {"name": "Alice"}})
        profile = self.backend.get_user_profile("user1")
        self.assertEqual(profile["profile"]["name"], "Alice")

        self.backend.update_user_profile("user1", {"name": "Updated Alice"})
        profile = self.backend.get_user_profile("user1")
        self.assertEqual(profile["profile"]["name"], "Updated Alice")

    def test_activate_deactivate_user(self):
        self.backend.create_user("user1", {"password": "pass123", "active": True})
        self.backend.deactivate_user("user1")
        self.assertFalse(self.mock_database["user1"]["active"])

        self.backend.activate_user("user1")
        self.assertTrue(self.mock_database["user1"]["active"])

    def test_get_active_inactive_users(self):
        self.backend.create_user("user1", {"password": "pass123", "active": True})
        self.backend.create_user("user2", {"password": "pass456", "active": False})
        active_users = self.backend.get_active_users()
        inactive_users = self.backend.get_inactive_users()
        self.assertIn("user1", active_users)
        self.assertIn("user2", inactive_users)

if __name__ == "__main__":
    unittest.main()
