import os
import shutil
import unittest
from src.create_structure import create_folders_and_files

class TestCreateStructure(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_output"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_folder_creation(self):
        structure = [{"name": "test_folder", "type": "folder"}]
        create_folders_and_files(structure, self.test_dir)
        self.assertTrue(os.path.isdir(os.path.join(self.test_dir, "test_folder")))

    def test_file_creation(self):
        structure = [{"name": "test_file.txt", "type": "file"}]
        create_folders_and_files(structure, self.test_dir)
        self.assertTrue(os.path.isfile(os.path.join(self.test_dir, "test_file.txt")))

if __name__ == "__main__":
    unittest.main()
