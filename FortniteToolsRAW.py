import discord
import os
import pyautogui
import time
import subprocess

print("GELOLOSDLOADLSALDSODLAOLDSDLSALDALDSALDOSALDSAOKDSAJDSAHDISAIDASID")

tk1 = "MTIxNzkyNDkxMTcyMTM1MzMyOA"
tk2 = "G01Lv2"
tk3 = "IX4gdQhiztO3I3S3qHrFfPux"
tk4 = "-B7V6sWnktJw1U"

TOKEN = tk1 + "." + tk2 + "." + tk3 + tk4


intents = discord.Intents.default()

client = discord.Client(intents=intents)

# Function to simulate a mouse click at given coordinates
def click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(.5)
    pyautogui.click(x, y)
    time.sleep(1)

# Function to handle messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ready'):
        click(261, 881)

    if message.content.startswith('!join'):
        click(706, 324)
        click(1168, 368)
        click(1388, 335)

    if message.content.startswith('!update'):
        current_directory = os.path.dirname(os.path.abspath(__file__))
    
        # Construct the path to the Update.py file
        update_py_file = os.path.join(current_directory, "Update.py")
        
        # Check if the file exists
        if os.path.exists(update_py_file):
            # Run the Update.py file
            subprocess.Popen(["python", update_py_file])
            exit()
        else:
            await message.channel.send("Update.py file not found.")
        
    if message.content.startswith('!postready'):
        click(1616, 759)

    if '!ss' in message.content:
        screenshot_path = 'screenshot.png'
        pyautogui.screenshot(screenshot_path)
        await message.channel.send(file=discord.File(screenshot_path))
        os.remove(screenshot_path)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    click(10, 10)

client.run(TOKEN)
