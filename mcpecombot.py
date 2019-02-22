import discord
from discord.ext import commands

import datetime

client = commands.Bot(command_prefix=".")

TOKEN = "NTQ2MzMxNjEzNTc5OTY4NTMw.D1FA-g.sKso2nlghK9a4YyP1oY2ak8NqZo"


@client.event
async def on_ready():
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
    embed = discord.Embed(title="Title", description="Description", colour=discord.Color.green(),
                          url="https://www.google.com")

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://discordpy.readthedocs.io/en/rewrite/_images/snake.png")
    embed.set_thumbnail(url="https://www.python.org/static/img/python-logo.png")

    embed.add_field(name="Field 1", value="value 1")
    embed.add_field(name="Field 2", value="value 2")

    embed.add_field(name="Field 3", value="value 3", inline=False)
    embed.add_field(name="Field 4", value="value 4")

    await ctx.send(embed=embed)


client.run(TOKEN)
