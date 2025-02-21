import argparse
from src.create_structure import create_folders_and_files 
from src.parser import parse_structure

def main():
    parser = argparse.ArgumentParser(description="Folder Structure CLI Tool")
    parser.add_argument("structure_file", help="Path to the structure file (YAML or TXT)")
    parser.add_argument("output_directory", help="Target directory for the structure")
    
    args = parser.parse_args()

    structure = parse_structure(args.structure_file)
    create_folders_and_files(structure, args.output_directory)
    print(f"✅ Structure created successfully in {args.output_directory}")

if __name__ == "__main__":
    main()
