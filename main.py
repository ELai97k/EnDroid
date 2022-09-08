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
    await client.change_presence(
        activity = discord.Activity(
            type = discord.ActivityType.playing, name = "Visual Studio Code"
        )
    )

# add default prefix and guild id to json file when bot joins server
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    # default prefix
    prefixes[str(guild.id)] = "?"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

# remove prefix and guild id from json file when bot leaves server
@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


# on message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return

    # shut up bot
    if "shut up bot" in message.content.lower() or "shut up endroid" in message.content.lower() or "endroid shut up" in message.content.lower() or "bot shut up" in message.content.lower():
        await message.channel.send("Okay :(")
        client.unload_extension("cogs.auto_responses")
        print("Auto Responses has been turned off")
        await asyncio.sleep(999)
        client.load_extension("cogs.auto_responses")
        print("Auto Responses has been turned on")
    
    await client.process_commands(message)


# auto responses off
@client.command(pass_context=True)
async def autoresponse_off(ctx):
    if ctx.author == client.user:
        return
    if ctx.author.bot:
        return

    embed = discord.Embed (
        title = "Operation Successful!",
        description = "`Auto-Responses` has been turned **OFF** and your changes were saved.",
        color=0x198C19
    )
    await ctx.send(embed=embed)
    client.unload_extension("cogs.auto_responses")
    print("Auto responses has been turned off")

# auto responses on
@client.command(pass_context=True)
async def autoresponse_on(ctx):
    if ctx.author == client.user:
        return
    if ctx.author.bot:
        return

    embed = discord.Embed (
        title = "Operation Successful!",
        description = "`Auto-Responses` has been turned **ON** and your changes were saved.",
        color=0x198C19
    )
    await ctx.send(embed=embed)
    client.load_extension("cogs.auto_responses")
    print("Auto responses has been turned on")


client.run(os.getenv('TOKEN'))