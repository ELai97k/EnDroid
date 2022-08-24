import discord
from discord.ext import commands
import os
import asyncio
import json


intents = discord.Intents.default().all()
intents.members = True


# setting up prefixes.json as json file
def get_prefix(client, message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  return prefixes[str(message.guild.id)]

def get_prefix(client=None, message=None):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  try:
    prefix = str(message.guild.id)
    return prefixes[prefix]

  except AttributeError:
    return ['defaultPrefix']

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
    activity = discord.Activity (
      type = discord.ActivityType.playing, name = "Visual Studio Code"
    )
  )


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
  embed = discord.Embed (
    title="Operation Successful!",
    description="`Auto-Responses` has been turned **OFF** and your changes were saved.",
    color=0x198C19
  )
  await ctx.send(embed=embed)
  client.unload_extension("cogs.auto_responses")
  print("Auto responses turned off")

# auto responses on
@client.command(pass_context=True)
async def autoresponse_on(ctx):
  embed = discord.Embed (
    title="Operation Successful!",
    description="`Auto-Responses` has been turned **ON** and your changes were saved.",
    color=0x198C19
  )
  await ctx.send(embed=embed)
  client.load_extension("cogs.auto_responses")
  print("Auto responses turned on")


client.run(os.getenv('TOKEN'))