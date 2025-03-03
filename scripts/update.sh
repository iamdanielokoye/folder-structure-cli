#!/bin/bash

# Pull the latest changes from the repository (adjust branch if needed)
git pull origin main

pip install --user pipx
pipx ensurepath

# Reinstall the package (from the project root)
pipx install -e ./scripts