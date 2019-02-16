import discord
from discord.ext import commands

TOKEN = 'NTQ2MzMxNjEzNTc5OTY4NTMw.D0nDDQ.tjiYDDBG-zZoApoD_PAmzt0GKQw'

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print ('Logged in')

client.run(TOKEN)