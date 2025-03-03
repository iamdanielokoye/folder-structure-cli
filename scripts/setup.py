import os
from setuptools import setup, find_packages

def get_version():
    version_path = os.path.join(os.path.dirname(__file__), "../version.py")
    try:
        with open(version_path, "r") as f:
            for line in f:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"')
    except FileNotFoundError:
        print(f"Error: version.py not found at {version_path}")
        return "0.0.0"
    except Exception as e:
        print(f"Error reading version.py: {e}")
        return "0.0.0"

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
