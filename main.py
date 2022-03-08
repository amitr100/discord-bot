import discord
import os
import random
import requests
import json
from datetime import datetime
now = datetime.now()

client = discord.Client()
habits = ["read","play music","bake","game","exercise"]
location=["my home","jack's home","playground"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    msg = message.content

    if any(now.minute %2 == 0):  
     await message.channel.send('I will '+random.choice(habits)+' in '+random.choice(location))   

client.run(os.getenv('TOKEN'))