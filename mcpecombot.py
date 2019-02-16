import discord
from discord.ext import commands

TOKEN = 'NTQ2MzMxNjEzNTc5OTY4NTMw.D0nDDQ.tjiYDDBG-zZoApoD_PAmzt0GKQw'

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print ('Logged in')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))

client.run(TOKEN)
