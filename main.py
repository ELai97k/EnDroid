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


# add default prefix and guild id to json file when bot joins server
@client.event
async def on_guild_join(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  # default prefix
  prefixes[str(guild.id)] = "?/"

  with open("prefixes.json", "w") as f:
    json.dump(prefixes, f, indent=4)

# remove prefix and guild id from json file
@client.event
async def on_guild_remove(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  prefixes.pop(str(guild.id))

  with open("prefixes.json", "w") as f:
    json.dump(prefixes, f, indent=4)


# change prefix command
@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  prefixes[str(ctx.guild.id)] = prefix

  with open("prefixes.json", "w") as f:
    json.dump(prefixes, f, indent=4)

  embed = discord.Embed (
    title="The bot's default prefix has been changed",
    color=0xc7ecf7
  )
  embed.add_field (name="Default prefix",
      value="?/",
      inline=False)

  embed.add_field (name="New prefix",
      value=f"{prefix}",
      inline=False)
      
  await ctx.send(embed=embed)
    

# on message event
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # current prefix command
  if message.content.lower().startswith("what is the current prefix") or message.content.lower().startswith("whats the current prefix") or message.content.lower().startswith("what's the current prefix"):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
      prefix = prefixes[str(message.guild.id)]

      await message.channel.trigger_typing()
      await message.channel.send(f"The current prefix is set to `{prefix}`")
  
  # shut up bot
  if "shut up bot" in message.content.lower() or "shut up endroid" in message.content.lower():
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