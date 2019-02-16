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

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('?ping'):
        await client.send_message(channel, 'Pong!')

    if message.content.startswith('?echo'):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await client.send_message(channel, output)

client.run(TOKEN)
