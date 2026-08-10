# test_autoalliance.py
"""
Tests for AutoAlliance module.
"""

import unittest
from autoalliance import AutoAlliance

class TestAutoAlliance(unittest.TestCase):
    """Test cases for AutoAlliance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoAlliance()
        self.assertIsInstance(instance, AutoAlliance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoAlliance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
