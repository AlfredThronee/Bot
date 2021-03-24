import discord
from discord import Embed, File
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Da Bot Yeah Yeah!')
    activity = discord.Activity(name='you all', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

    channel = client.get_channel(823835795726925834)
    embed = Embed(title="Now online! Yeah Yeah!", description="Da Bot is here.")
    fields = [("I go where i want", "Good", True),
              ("Play if you want", "Lets do it", True),
              ("Im the young CEO", "Suge, yeah yeah!", True)]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await channel.send(embed=embed)

@client.event
#We create an on message event
async def on_message(message):
    #We check if the the message that has been sent equals react
    if message.author.id == 202061409545093120 and message.content.lower() == 'react':
        await message.channel.send('reacted!')

@client.command()
async def vibez(ctx):
    channel = client.get_channel(823835795726925834)
    await channel.send('LETS GOOOO')

@client.command()
async def ping(ctx):
    channel = client.get_channel(823835795726925834)
    await channel.send(f'Pong! {round(client.latency * 1000)}ms')
    
client.run('token')
