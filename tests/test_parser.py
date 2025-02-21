# test_parser.py
import unittest
from src.parser import parse_yaml_string

class TestParser(unittest.TestCase):
    def test_parse_yaml(self):
        yaml_data = """
        project:
          - README.md
          - src:
              - main.py
              - utils.py
        """
        expected_output = [{'name': 'project', 'type': 'folder', 'children': [
            {'name': 'README.md', 'type': 'file'},
            {'name': 'src', 'type': 'folder', 'children': [
                {'name': 'main.py', 'type': 'file'},
                {'name': 'utils.py', 'type': 'file'}
            ]}
        ]}]
        self.assertEqual(parse_yaml_string(yaml_data), expected_output)

if __name__ == "__main__":
    unittest.main()