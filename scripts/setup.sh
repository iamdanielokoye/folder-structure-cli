#!/bin/bash

echo "📦 Setting up the folder-cli..."

# Ensure pip and setuptools are up to date
pip install --upgrade pip setuptools wheel

# Install pipx
pip install --user pipx
pipx ensurepath

# Install the CLI tool
pipx install -e ./scripts

echo "✅ Setup Complete! You can now run 'folder-cli --help'"
