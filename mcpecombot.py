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
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))
    await client.process_commands(message)

@client.command()
async def ping ():
    await client.say('Pong!')
    await client.process_commands(message)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    await client.process_commands(message)

    client.run(TOKEN)
