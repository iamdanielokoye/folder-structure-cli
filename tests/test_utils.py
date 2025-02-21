# test_utils.py
import unittest
import os
from src.create_structure import create_structure
import sys

sys.path.insert(0, '../src')

class TestUtils(unittest.TestCase):
    def test_create_structure(self):
        structure = {'test_project': ['README.md', {'src': ['main.py']}]}
        base_path = "test_output"
        create_structure(structure, base_path)
        self.assertTrue(os.path.exists(os.path.join(base_path, "test_project", "README.md")))
        self.assertTrue(os.path.exists(os.path.join(base_path, "test_project", "src", "main.py")))

if __name__ == "__main__":
    unittest.main()