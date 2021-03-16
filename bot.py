import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Alfreds skapelse lever!')

client.run('ODIxMjkxMzUxMjEwNzIxMjgw.YFBlLA.3xeGMDBL46DzqFhpMADeH9KsoR8')