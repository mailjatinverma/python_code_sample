"""Module for testing the Settings module functionality"""
import unittest

from python_code_sample.settings import Settings


class SettingsTest(unittest.TestCase):
    """Class to test the settings class functionality"""

    @classmethod
    def setUpClass(cls):
        """set up method"""
        # create user 'user' with password '12345'
        # Mock DB calls
        pass


    @classmethod
    def tearDownClass(cls):
        """ tear down method"""
        pass

    def test_set_account_new_password(self):
        """method to test the set_account_new_password functionality of Settings module"""
        # Positive Case
        self.assertEquals(Settings.set_account_new_password('user', '12345', 'abcde', 'abcde'), 0)
        # Negative Cases
        self.assertEquals(Settings.set_account_new_password('user', '123456', 'abcde', 'abcde'), 1)
        self.assertEquals(Settings.set_account_new_password('user', 'abcde', 'abcdef', 'abcdeg'), 2)
        self.assertEquals(Settings.set_account_new_password('user', 'abcdef', '12345', '123456'), 2)
        # Edge Case - bug found. :)
        self.assertEquals(Settings.set_account_new_password('user', 'abcde', '', ''), 0)
