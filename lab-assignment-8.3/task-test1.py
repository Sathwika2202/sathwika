import unittest
from TAsk1 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("user@example.com"))

    def test_no_at_symbol(self):
        self.assertFalse(is_valid_email("userexample.com"))

    def test_multiple_at_symbols(self):
        self.assertFalse(is_valid_email("user@@example.com"))

    def test_no_dot(self):
        self.assertFalse(is_valid_email("user@examplecom"))

    def test_starts_with_special_char(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("@user@example.com"))

    def test_ends_with_special_char(self):
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("user@example.com@"))

    def test_dot_before_at(self):
        self.assertTrue(is_valid_email("user.name@example.com"))

    def test_dot_after_at(self):
        self.assertTrue(is_valid_email("user@example.co.uk"))

    def test_only_special_chars(self):
        self.assertFalse(is_valid_email("@."))

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

if __name__ == "__main__":
    unittest.main()
