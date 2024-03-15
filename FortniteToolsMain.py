import requests

def execute_code_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        exec(code)  # or eval(code) depending on the use case
    else:
        print("Failed to fetch code from URL")

# Example usage:
url = "https://raw.githubusercontent.com/SSkiprs/FortniteTools/FortniteTools/FortniteToolsRAW.py"  # Replace with the actual URL
execute_code_from_url(url)
