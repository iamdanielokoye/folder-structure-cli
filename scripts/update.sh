#!/bin/bash

echo "Updating Folder Structure CLI Tool to the latest version..."

git pull origin main

pipx install --force -e ./scripts

echo "✅ CLI Tool updated successfully"

pipx ensurepath

echo "✅ Path updated successfully, restart your terminal to see changes!"