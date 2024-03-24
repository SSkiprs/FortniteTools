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

Locked = False  # Initialize as boolean

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
    global Locked  # Declare as global

    if message.author == client.user:
        return

    if message.content.startswith('!lock'):
        if message.author.id == 858825984340656169:
            Locked = True
            await message.channel.send("Successfully locked!")

    if message.content.startswith('!unlock'):
        if message.author.id == 858825984340656169:
            Locked = False
            await message.channel.send("Successfully unlocked!")

    if message.content.startswith('!ready'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            click(261, 881)
            await message.channel.send("Clicked Ready!")

    elif message.content.startswith('!join'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            click(706, 324)
            click(1168, 368)
            click(1388, 335)
            await message.channel.send("Clicked Join!")

    elif message.content.startswith('!lobby'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            pyautogui.press('esc')
            click(1317, 1010)
            click(1647, 1022)
            click(1521, 1020)
            await message.channel.send("Entered Lobby!")

    elif message.content.startswith('!debug'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            pyautogui.press('esc')
            pyautogui.press('esc')
            click(10, 10)
            await message.channel.send("Entered Debug Mode!")

    elif message.content.startswith('!postready1'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            await message.channel.send("This feature is still in development!")

    elif message.content.startswith('!update'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            update_py_file = os.path.join(current_directory, "Update.py")
            if os.path.exists(update_py_file):
                subprocess.Popen(["python", update_py_file])
                await message.channel.send("Update initiated.")
                exit()
            else:
                await message.channel.send("Update.py file not found.")

    elif message.content.startswith('!postready'):
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            click(1616, 759)
            await message.channel.send("Clicked Post Ready!")

    elif '!ss' in message.content:
        if Locked:
            # Locked
            await message.channel.send("I am currently locked! Check back soon...")
            pass
        else:
            screenshot_path = 'screenshot.png'
            pyautogui.screenshot(screenshot_path)
            await message.channel.send(file=discord.File(screenshot_path))
            os.remove(screenshot_path)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send("I'm connected and ready to roll!")

client.run(TOKEN)
