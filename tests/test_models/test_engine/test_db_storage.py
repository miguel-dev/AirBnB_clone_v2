#!/usr/bin/python3
"""Tests DB Storage"""
import unittest


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                 "Skip if db storage is enabled")
class TestDBSTorage(unittest.TestCase):
    """Class for testing DB Storage"""

    def test_save(self):
        """Tests save"""
        pass

if __name__ == '__main__':
    unittest.main()
