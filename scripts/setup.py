from setuptools import setup, find_packages

setup(
    name="folder-structure-cli",
    version="0.1.0",
    packages=find_packages(where="src"),  # Look for packages inside 'src'
    package_dir={"": "src"},  # Treat 'src' as the root package directory
    install_requires=[
        "PyYAML",  # Add other dependencies if necessary
    ],
    entry_points={
        "console_scripts": [
            "folder-cli=cli:main",  # Calls the main() function in cli.py
        ],
    },
)
