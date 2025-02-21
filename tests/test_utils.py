# test_utils.py
import unittest
import os
from src.create_structure import create_folders_and_files

class TestUtils(unittest.TestCase):
    def test_create_structure(self):
        structure = [
            {"name": "test_project", "type": "folder", "children": [
                {"name": "README.md", "type": "file"},
                {"name": "src", "type": "folder", "children": [
                    {"name": "main.py", "type": "file"}
                ]}
            ]}
        ]
        base_path = "test_output"
        create_folders_and_files(structure, base_path)
        self.assertTrue(os.path.exists(os.path.join(base_path, "test_project", "README.md")))
        self.assertTrue(os.path.exists(os.path.join(base_path, "test_project", "src", "main.py")))

if __name__ == "__main__":
    unittest.main()