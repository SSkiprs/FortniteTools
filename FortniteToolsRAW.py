import discord
import os
import pyautogui
import time
import subprocess

# Your token parts
tk1 = "MTIxNzkyNDkxMTcyMTM1MzMyOA"
tk2 = "G01Lv2"
tk3 = "IX4gdQhiztO3I3S3qHrFfPux"
tk4 = "-B7V6sWnktJw1U"
TOKEN = f"{tk1}.{tk2}.{tk3}{tk4}"

# Channel ID to send the message to
channel_id = 1080579533691953162

# User ID to lock/unlock commands
locked_user_id = 858825984340656169

class CommandLock:
    def __init__(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def is_locked(self):
        return self.locked

lock = CommandLock()

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Function to simulate a mouse click at given coordinates
def click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(1)

# Function to handle messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the user is locked
    if lock.is_locked() and message.author.id != locked_user_id:
        await message.channel.send("I am currently locked. Check back soon.")
        return

    if message.content.startswith('!ready'):
        click(261, 881)
        await message.channel.send("Clicked Ready!")

    elif message.content.startswith('!join'):
        click(706, 324)
        click(1168, 368)
        click(1388, 335)
        await message.channel.send("Clicked Join!")

    elif message.content.startswith('!lobby'):
        pyautogui.press('esc')
        click(1317, 1010)
        click(1647, 1022)
        click(1521, 1020)
        await message.channel.send("Entered Lobby!")

    elif message.content.startswith('!debug'):
        pyautogui.press('esc')
        pyautogui.press('esc')
        click(10, 10)
        await message.channel.send("Entered Debug Mode!")

    elif message.content.startswith('!postready1'):
        # Define your click coordinates here
        # click(x, y)
        await message.channel.send("Clicked Post Ready 1!")

    elif message.content.startswith('!update'):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        update_py_file = os.path.join(current_directory, "Update.py")
        if os.path.exists(update_py_file):
            subprocess.Popen(["python", update_py_file])
            await message.channel.send("Update initiated.")
            exit()
        else:
            await message.channel.send("Update.py file not found.")

    elif message.content.startswith('!postready'):
        click(1616, 759)
        await message.channel.send("Clicked Post Ready!")

    elif '!ss' in message.content:
        screenshot_path = 'screenshot.png'
        pyautogui.screenshot(screenshot_path)
        await message.channel.send(file=discord.File(screenshot_path))
        os.remove(screenshot_path)
    
    elif message.content.startswith('!lock') and message.author.id == locked_user_id:
        lock.lock()
        await message.channel.send("Commands locked!")

    elif message.content.startswith('!unlock') and message.author.id == locked_user_id:
        lock.unlock()
        await message.channel.send("Commands unlocked!")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send("I'm connected and ready to roll!")

client.run(TOKEN)
