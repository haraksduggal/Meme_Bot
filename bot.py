import discord
import requests
import json


with open("bot_token.txt","r") as f:
    TOKEN = f.readline()

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


intents = discord.Intents.default()
intents.message_content = True #Necessary for reading messages.

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$meme'):
        await message.channel.send(get_meme())

client.run(TOKEN)
