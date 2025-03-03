#!/bin/bash

echo "Updating Folder Structure CLI Tool to the latest version..."

git pull origin main

pipx install --force -e .

echo "✅ CLI Tool updated successfully"