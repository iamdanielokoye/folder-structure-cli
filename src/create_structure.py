import os
import sys
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
            open(path, 'w').close()  # Create empty file

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
