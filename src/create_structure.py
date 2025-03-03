import os
import sys
import json
import yaml
from src.parser import parse_structure

def create_folders_and_files(structure, base_path):
    """
    Recursively creates folders and files from a parsed structure.
    """
    for item in structure:
        path = os.path.join(base_path, item["name"])

        if item["type"] == "folder":
            os.makedirs(path, exist_ok=True)
            if "children" in item:
                create_folders_and_files(item["children"], path)
        elif item["type"] == "file":
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8'):
                pass  # Create an empty file

def create_structure_from_text(file_path, base_path):
    """
    Parses a tree-like structured text file and creates the directory structure.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        stack = []
        last_depth = -1

        for line in lines:
            depth = line.count('│') + line.count('├') + line.count('└')
            name = line.strip().replace('├──', '').replace('└──', '').replace('│', '').strip()

            if not name:
                continue
            
            # Ensure stack matches depth
            while len(stack) > depth:
                stack.pop()

            # Build full path
            current_path = os.path.join(base_path, *stack)

            # Ensure current_path is a valid string before joining
            full_path = os.path.join(current_path, name)

            if '.' in name:  # File
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w', encoding='utf-8'):
                    pass  # Create an empty file
            else:  # Directory
                os.makedirs(full_path, exist_ok=True)
                stack.append(name)

        print("✅ Successfully created structure using tree-based indentation.")

    except Exception as e:
        print(f"❌ Failed to create structure using tree indentation: {e}")

def create_structure_from_yaml(file_path, base_path):
    """Parses a YAML file and creates the directory structure properly."""
    def create_from_dict(base_path, structure):
        for key, value in structure.items():
            path = os.path.join(base_path, key)
            if isinstance(value, dict):
                os.makedirs(path, exist_ok=True)
                create_from_dict(path, value)
            else:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w', encoding='utf-8'):
                    pass  # Create an empty file

    with open(file_path, 'r', encoding='utf-8') as file:
        structure = yaml.safe_load(file)
        create_from_dict(base_path, structure)

def create_structure_from_json(file_path, base_path):
    """
    Parses a JSON file and creates the directory structure.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            structure = json.load(file)

        def create_structure(structure, base_path):
            for item in structure:
                name = item["name"]
                item_type = item["type"]
                full_path = os.path.join(base_path, name)

                if item_type == "folder":
                    os.makedirs(full_path, exist_ok=True)
                    if "children" in item:
                        create_structure(item["children"], full_path)
                elif item_type == "file":
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, 'w', encoding='utf-8'):
                        pass  # Create an empty file

        create_structure(structure, base_path)
        print("✅ Successfully created structure using JSON format.")

    except Exception as e:
        print(f"❌ Failed to create structure using JSON format: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python create_structure.py <structure_file> <output_directory>")
        sys.exit(1)

    structure_file = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)

    if structure_file.endswith('.json'):
        create_structure_from_json(structure_file, output_directory)
    elif structure_file.endswith('.txt'):
        create_structure_from_text(structure_file, output_directory)
    elif structure_file.endswith('.yaml') or structure_file.endswith('.yml'):
        create_structure_from_yaml(structure_file, output_directory)
    else:
        structure = parse_structure(structure_file)
        if structure is None:
            print(f"❌ Failed to parse structure file: {structure_file}")
            return
        create_folders_and_files(structure, output_directory)
    print(f"✅ Folder structure created successfully in: {output_directory}")

if __name__ == "__main__":
    main()
