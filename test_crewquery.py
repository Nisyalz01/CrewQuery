# test_crewquery.py
"""
Tests for CrewQuery module.
"""

import unittest
from crewquery import CrewQuery

class TestCrewQuery(unittest.TestCase):
    """Test cases for CrewQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrewQuery()
        self.assertIsInstance(instance, CrewQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrewQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
