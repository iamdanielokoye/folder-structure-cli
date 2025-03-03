#!/bin/bash

echo "Updating Folder Structure CLI Tool to the latest version..."

git pull origin main

pip install requests
pipx install --force -e ./scripts

echo "✅ CLI Tool updated successfully"