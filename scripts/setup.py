import os
from setuptools import setup, find_packages

def get_version():
    version_path = os.path.join(os.path.dirname(__file__), "../version.py") # Adjust path if needed
    with open(version_path, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')
    return "0.0.0" # Default version if not found

setup(
    name="folder-structure-cli",
    version=get_version(),
    packages=find_packages(where="../src"),  # Look for packages inside 'src'
    package_dir={'': '..'},  # Treat 'src' as the root package directory
    install_requires=[
        'PyYAML==6.0.2',  # Pin the versions here, too
        'requests==2.32.3',
        'certifi==2025.1.31',
        'charset-normalizer==3.4.1',
        'idna==3.10',
        'urllib3==2.3.0',
    ],
    entry_points={
        "console_scripts": [
            "folder-cli=src.cli:main",  # Calls the main() function in cli.py
        ],
    },
)
