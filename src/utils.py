import os

def validate_path(path):
    """
    Ensures the path is valid and creates it if necessary.
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def print_success_message(output_directory):
    """
    Prints a success message.
    """
    print(f"✅ Folder structure successfully created in: {output_directory}")
