# Usage Guide

## Creating a Folder Structure

### Basic Usage

    python src/cli.py <structure_file> <output_directory>

`structure_file`: The YAML or text file defining the folder structure.

`output_directory`: The location where the structure will be created.

### Example

- Using a YAML File

        python src/cli.py examples/structure.yaml my_project

- Using a Text File

        python src/cli.py examples/structure.txt my_project

### File Formats

- YAML Format Example

        project-name:
        - README.md
        - src:
            - main.py
            - utils.py
        - tests:
            - test_main.py

- TXT Format Example

        project-name/
            README.md
            src/
                main.py
                utils.py
            tests/
                test_main.py

### Running Tests

To verify everything is working correctly, run:

        python -m unittest discover tests