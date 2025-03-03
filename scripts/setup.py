import os
from setuptools import setup, find_packages

setup(
    name="folder-structure-cli",
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
