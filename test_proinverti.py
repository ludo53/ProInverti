# test_proinverti.py
"""
Tests for ProInverti module.
"""

import unittest
from proinverti import ProInverti

class TestProInverti(unittest.TestCase):
    """Test cases for ProInverti class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProInverti()
        self.assertIsInstance(instance, ProInverti)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProInverti()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
