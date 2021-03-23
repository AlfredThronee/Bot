import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Alfreds skapelse lever!')
    activity = discord.Activity(name='you all', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

@client.command()
async def game(ctx):
    channel = client.get_channel(823835795726925834)
    await channel.send('gaming')

@client.command()
async def ping(ctx):
    channel = client.get_channel(823835795726925834)
    await channel.send(f'Pong! {round(client.latency * 1000)}ms')

client.run('token')
