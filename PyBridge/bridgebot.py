from colorama import Fore
from pathlib import Path
import discord
import json
import os

# Do NOT move this or it will break
os.chdir(Path(__file__).parent)

try:
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

except FileNotFoundError:
    print(Fore.RED + "| [ERROR] settings.json file not found!")

except json.JSONDecodeError:
    print(Fore.RED + "| [ERROR] Couldn't decode JSON from file! This is caused by errors in the JSON code. (malformed)")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

    if message.channel.id == 1405277067309879376 and not message.webhook_id :
        print(f'{message.author}: {message.content} ')

client.run(str({settings["botDcToken"]}))