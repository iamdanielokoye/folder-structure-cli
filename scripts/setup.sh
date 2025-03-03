#!/bin/bash

echo "📦 Setting up the folder-cli..."

# Ensure pip and setuptools are up to date
pip install --upgrade pip setuptools wheel

# Install the CLI tool
pip install -e ./scripts

echo "✅ Setup Complete! You can now run 'folder-cli --help'"
