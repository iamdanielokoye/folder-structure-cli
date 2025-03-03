#!/bin/bash

echo "Updating Folder Structure CLI Tool to the latest version..."

git pull origin main

pipx install --force -e ./scripts

echo "✅ CLI Tool updated successfully"

# Fetch and display the latest release tag from GitHub
latest_tag=$(curl -s "https://api.github.com/repos/iamdanielokoye/folder-structure-cli/releases/latest" | jq -r '.tag_name')

if [ -n "$latest_tag" ]; then
  echo "Latest release tag from GitHub: $latest_tag"
else
  echo "Failed to fetch latest release tag from GitHub."
fi