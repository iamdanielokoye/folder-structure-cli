import os
import sys
from src.parser import parse_structure

def create_structure_from_text(file_path, base_path):
    """
    Parses a tree-like structured text file and creates the directory structure.
    Example:
        project
        ├── src
        │   ├── main.py
        │   ├── utils.py
        └── README.md
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        stack = []
        for line in lines:
            depth = line.count('│') + line.count('├') + line.count('└')
            name = line.strip().replace('├──', '').replace('└──', '').replace('│', '').strip()

            if not name:
                continue

            while len(stack) > depth:
                stack.pop()

            current_path = os.path.join(base_path, *stack, name)

            if '.' in name:  # File
                open(current_path, 'w').close()
            else:  # Directory
                os.makedirs(current_path, exist_ok=True)
                stack.append(name)

        print("✅ Successfully created structure using tree-based indentation.")

    except Exception as e:
        print(f"❌ Failed to create structure using tree indentation: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python create_structure.py <structure_file> <output_directory>")
        sys.exit(1)

    structure_file = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)

    structure = parse_structure(structure_file)
    create_folders_and_files(structure, output_directory)
    print(f"✅ Folder structure created successfully in: {output_directory}")

if __name__ == "__main__":
    main()
