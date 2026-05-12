# Examples: Testing a Calculator and String Utils

import unittest

# --- The Code to Test ---
class SimpleMath:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# --- The Test Suite ---
class TestSimpleMath(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test. Useful for shared initialization."""
        print("\nSetting up a test...")
        self.math = SimpleMath()

    def test_add_positive(self):
        """Test adding two positive numbers."""
        result = self.math.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_negative(self):
        """Test adding negative numbers."""
        result = self.math.add(-1, -1)
        self.assertEqual(result, -2)

    def test_divide_normal(self):
        """Test normal division."""
        self.assertEqual(self.math.divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.math.divide(10, 0)

    def tearDown(self):
        """Runs after every test."""
        print("Cleaning up after test.")

# --- Running the Tests ---
if __name__ == "__main__":
    # In a script, this is how you trigger the unittest runner
    unittest.main()
