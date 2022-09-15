import discord
import os
import asyncio
import json
from discord.ext import commands

intents = discord.Intents.default().all()
intents.members=True

# setting up prefixes.json in json file
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)


# cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename [:-3]}')


# on ready event
@client.event
async def on_ready():
    # bot login
    print(f"{client.user} logged in successfully!")

    # bot default status
    await client.change_presence (
        activity = discord.Activity (
            type = discord.ActivityType.playing, name = "Visual Studio Code"
        )
    )


client.run(os.getenv('TOKEN'))