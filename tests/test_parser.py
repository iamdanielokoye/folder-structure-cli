# test_parser.py
import unittest
from src.parser import parse_structure

class TestParser(unittest.TestCase):
    def test_parse_yaml(self):
        yaml_data = """
        project:
          - README.md
          - src:
              - main.py
              - utils.py
        """
        expected_output = {'project': ['README.md', {'src': ['main.py', 'utils.py']}]}
        self.assertEqual(parse_structure(yaml_data, 'yaml'), expected_output)

if __name__ == "__main__":
    unittest.main()