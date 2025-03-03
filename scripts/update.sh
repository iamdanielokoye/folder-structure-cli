#!/bin/bash

# Pull the latest changes from the repository (adjust branch if needed)
git pull origin main

# Reinstall the package (from the project root)
pip install -e ./scripts