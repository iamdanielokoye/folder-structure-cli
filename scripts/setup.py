import requests
from setuptools import setup, find_packages

def get_latest_release_tag():
    url = "https://api.github.com/repos/iamdanielokoye/folder-structure-cli/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    return latest_release["tag_name"]

setup(
    name="folder-structure-cli",
    version=get_latest_release_tag(),
    packages=find_packages(where="../src"),  # Look for packages inside 'src'
    package_dir={'': '..'},  # Treat 'src' as the root package directory
    install_requires=[
        'requests',  # Ensure requests is installed
    ],
    entry_points={
        "console_scripts": [
            "folder-cli=src.cli:main",  # Calls the main() function in cli.py
        ],
    },
)
