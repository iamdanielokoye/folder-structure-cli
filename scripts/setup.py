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
