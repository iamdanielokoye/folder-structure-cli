# Folder Structure CLI

A simple CLI tool to generate folder structures from YAML or text files.

# Installation Guide

## Prerequisites

Before installing, ensure you have the following installed on your system:

- Python (>= 3.8)
- Pip

## Installation

- Clone the Repository

        git clone https://github.com/iamdanielokoye/folder-structure-cli.git
        cd folder-structure-cli

- Navigate to the scripts Directory:

        cd scripts

- Make the Script Executable (you only need to do this once):

        chmod +x setup.sh

- Navigate back to the root directory and run the script:

        ./scripts/setup.sh #This will install the cli globally.

- Verify the installation

        folder-cli --help

If the installation is successful, you should see the usage guide.

## Usage Guide

### Basic Usage

        folder-cli <structure_file> <output_directory>

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

### 🎯 License

This project is licensed under the MIT License. See `LICENSE` for details.
