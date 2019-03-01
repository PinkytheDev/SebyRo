import discord
from discord import Game
from discord.ext import commands

import datetime

client = commands.Bot(command_prefix=".")

TOKEN = "NTQ2MzMxNjEzNTc5OTY4NTMw.D1FA-g.sKso2nlghK9a4YyP1oY2ak8NqZo"


@client.event
async def on_ready():
    await client.change_presence (game=Game (name="Give me the giveaway reward. SebyRo299") )
    print("Logged in as")
    print(client.user.name)
    print("---------------")


@client.event
async def on_message(message):
    user = message.author
    msg = message.content
    print(f"{user} : {msg}")
    await client.process_commands(message)


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))
    await client.process_commands(message)


@client.command()
async def ping():
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


@client.command()
async def embed(ctx):
    await client.say('Sorry failed. TROLOLOLOL')
    await client.process_commands(message)
    
    
@client.command(pass_context=True, adminstrator=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("{} Messages Deleted.".format(int(amount))

client.run(TOKEN)
