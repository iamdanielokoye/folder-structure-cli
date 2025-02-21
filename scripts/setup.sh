#!/bin/bash

echo "Setting up the folder-structure-cli..."

# Install project dependencies
pip install -r requirements.txt

# Install the package using setup.py (from the project root)
pip install -e ./scripts # Or pip install -e ./scripts if setup.py is there

echo "✅ Setup Complete!"