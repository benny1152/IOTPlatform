import repositories
import model
import unittest


class UserTests(unittest.TestCase):
    def __init__(self, testName):
        unittest.TestCase.__init__(self, testName)
        self.users = repositories.UserRepository(UserTests.collection)
        #self.users.clear_db()
        self.user1id = self.users.add_user("Benny Clark", "xxxxxxxx", "benny@example.com", False)
        self.user2id = self.users.add_user("Floris Kint", "xxxxxxxx", "floris@example.com", True)
        self.user3id = self.users.add_user("Ben Fossett", "xxxxxxxx", "ben@example.com", True)

    def test_UserAddedCorrectly(self):
        user3 = self.users.get_user_by_id(self.user3id)
        attributes = user3.get_user_attributes()
        self.assertEqual(attributes['name'], "Ben Fossett", "User name not added correctly.")
        self.assertEqual(attributes['password_hash'], "xxxxxxxx", "User password not added correctly.")
        self.assertEqual(attributes['email_address'], "ben@example.com", "User email not added correctly.")
        self.assertTrue(attributes['is_admin'], "User admin status not added correctly.")

    def test_UserRemovedCorrectly(self):
        all_users = self.users.get_all_users()
        self.users.remove_user(self.user3id)
        all_remaining_users = self.users.get_all_users()
        self.assertEqual(len(all_remaining_users), len(all_users) - 1, "A user has not been removed.")
