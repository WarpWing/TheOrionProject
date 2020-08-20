import os

import discord
from discord.ext.commands import Bot

token = ('TOKEN')
GUILD = ('656861178454081546')

client = discord.Client()
BOT_PREFIX = ("?", "!")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is loading up Modules!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    activity = discord.Game(name="Sentinel.SYS 3.5.1", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, you are here, now please get out'
    )


@client.event
async def on_message(message):
    if 'what is your purpose' in message.content.lower():
        await message.channel.send(' Being a Bot, thats it.....')


client.run(token)
