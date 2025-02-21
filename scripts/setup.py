from setuptools import setup, find_packages

setup(
    name='folder-structure-cli',
    version='0.1.0',
    package_dir={'': '..'}, # This line is important
    packages=find_packages(where='../src'), # This line is also important
    entry_points={
        'console_scripts': [
            'folder-structure = src.cli:main',  # If you have a main function
        ],
    },
)