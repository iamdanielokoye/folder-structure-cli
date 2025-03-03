#!/bin/bash

# 1. Pull the latest changes from the repository (adjust branch if needed)
git pull origin main

# 2. (Optional) Check for changes in requirements.txt and update if needed
if git diff --quiet requirements.txt; then  # Check if requirements.txt has changed
    echo "Requirements file has changed. Updating dependencies..."
    python3.12 -m pip install -r requirements.txt
else
    echo "No changes in requirements file."
fi

# 3. Reinstall the package (from the project root)
pip install -e ./scripts