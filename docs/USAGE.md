# Usage Guide

## Creating a Folder Structure

### Basic Usage

        python src/cli.py <structure_file> <output_directory>

`structure_file`: The YAML or text file defining the folder structure.

`output_directory`: The location where the structure will be created.

### Example

- Using a YAML File

        folder cli ./examples/text/structure.yaml ./  # Path to the YAML file in this project. The folders are created in the working directory.

- Using a Text File

        folder-cli ./examples/text/structure.txt # Path to the text file in this project. The folders are created in the working directory.

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