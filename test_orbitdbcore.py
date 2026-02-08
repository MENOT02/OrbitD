# test_orbitdbcore.py
"""
Tests for OrbitDBCore module.
"""

import unittest
from orbitdbcore import OrbitDBCore

class TestOrbitDBCore(unittest.TestCase):
    """Test cases for OrbitDBCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrbitDBCore()
        self.assertIsInstance(instance, OrbitDBCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrbitDBCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
