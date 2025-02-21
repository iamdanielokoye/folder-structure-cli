#!/bin/bash

echo "Cleaning up folder-structure-cli..."

# Remove installed package (if installed with pip install -e .)
pip uninstall -y folder-structure-cli  # -y skips confirmation

# Remove the build directory (if it exists)
if [ -d "build" ]; then
  rm -rf build
  echo "Removed build directory."
fi

# Remove the dist directory (if it exists)
if [ -d "dist" ]; then
  rm -rf dist
  echo "Removed dist directory."
fi

# Remove egg-info directory (if it exists)
if [ -d "folder_structure_cli.egg-info" ]; then  # Adjust if your project name is different
  rm -rf folder_structure_cli.egg-info
  echo "Removed egg-info directory."
fi

# Remove the .venv directory (if you used a virtual environment)
if [ -d ".venv" ]; then
  deactivate  # Deactivate the virtual environment (if it's active)
  rm -rf .venv
  echo "Removed virtual environment."
fi

# Remove __pycache__ directories (if they exist)
find . -name "__pycache__" -type d -exec rm -rf {} \;
echo "Removed __pycache__ directories."

# Optional: Remove any leftover .pyc files (compiled bytecode)
find . -name "*.pyc" -delete
echo "Removed .pyc files."

echo "Cleanup complete!"