import argparse
import requests
import os
import sys
import subprocess
from src.create_structure import create_folders_and_files, create_structure_from_text, create_structure_from_yaml, create_structure_from_json
from src.parser import parse_structure

def get_latest_release_tag():
    url = "https://api.github.com/repos/iamdanielokoye/folder-structure-cli/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    return latest_release["tag_name"]

def list_tags():
    tags = ["create_structure", "parse_yaml", "parse_text", "--update", "--version", "--dry-run", "--verbose", "--config", "--force"]
    print("Available tags:")
    for tag in tags:
        print(f"- {tag}")

def show_description():
    description = """
    Folder Structure CLI Tool
    This tool helps you create folder structures based on a given YAML, JSON, or TXT file.
    You can also list all available tags for the tool.
    """
    print(description)
    list_tags()

def update_tool():
    print("Updating Folder Structure CLI Tool to the latest version...")
    try:
        subprocess.run(["sh", "scripts/update.sh"], check=True)
        print("✅ Tool updated to the latest version.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to update the tool: {e}")

def main():
    parser = argparse.ArgumentParser(description="Folder Structure CLI Tool")
    parser.add_argument("structure_file", nargs='?', help="Path to the structure file (YAML, JSON, or TXT)")
    parser.add_argument("output_directory", nargs='?', help="Target directory for the structure")
    parser.add_argument("--list-tags", action="store_true", help="List all available tags")
    parser.add_argument("-u", "--update", action="store_true", help=get_latest_release_tag())
    parser.add_argument("-v", "--version", action="version", version="Folder Structure CLI Tool 1.0")
    parser.add_argument("-dr", "--dry-run", action="store_true", help="Simulate the creation of the folder structure")
    parser.add_argument("-vb", "--verbose", action="store_true", help="Provide detailed output of the operations")
    parser.add_argument("--config", help="Specify a configuration file for additional settings")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite existing files and directories without prompting")

    args = parser.parse_args()

    if args.list_tags:
        list_tags()
        return

    if args.update:
        update_tool()
        return

    if not args.structure_file or not args.output_directory:
        show_description()
        parser.print_help()
        return

    if args.structure_file.endswith('.json'):
        create_structure_from_json(args.structure_file, args.output_directory)
    elif args.structure_file.endswith('.txt'):
        create_structure_from_text(args.structure_file, args.output_directory)
    elif args.structure_file.endswith('.yaml') or args.structure_file.endswith('.yml'):
        create_structure_from_yaml(args.structure_file, args.output_directory)
    else:
        structure = parse_structure(args.structure_file)
        if structure is None:
            print(f"❌ Failed to parse structure file: {args.structure_file}")
            return
        create_folders_and_files(structure, args.output_directory)
    print(f"✅ Folder structure created successfully in: {args.output_directory}")

if __name__ == "__main__":
    main()
