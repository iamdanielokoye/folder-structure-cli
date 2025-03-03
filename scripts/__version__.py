import requests

def get_latest_release_tag():
    url = "https://api.github.com/repos/iamdanielokoye/folder-structure-cli/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    return latest_release["tag_name"]

__version__ = get_latest_release_tag()