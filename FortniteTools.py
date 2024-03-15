import discord
import os
import pyautogui
import time

TOKEN = 'MTIxNzkyNDkxMTcyMTM1MzMyOA.Go_uTW.hKrQqhD3LfZMHeXzqY2ZTI5H6vBYFcnRzP0sH8'

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

    elif message.content.startswith('!join'):
        click(706, 344)
        click(1168, 317)
        click(1388, 335)

    if '!ss' in message.content:
        screenshot_path = 'screenshot.png'
        pyautogui.screenshot(screenshot_path)
        await message.channel.send(file=discord.File(screenshot_path))
        os.remove(screenshot_path)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
