import discord
from discord.ext import commands
import json

class Prefix(commands.Cog):
    """Set up bot's default prefix when joining server and commands for changing bot prefix"""
    def __init__(self, client):
        self.client = client

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


    # add default prefix and guild id to json file when bot joins server
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        # default prefix
        prefixes[str(guild.id)] = "?"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    # remove prefix and guild id from json file when bot leaves server
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    
    # change prefix command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        embed = discord.Embed (
            title="The bot's default prefix has been changed",
            color=0xc7ecf7
        )
        embed.add_field(
            name="Default prefix",
            value="?/",
            inline=False
        )
        embed.add_field(
            name="New prefix",
            value=f"{prefix}",
            inline=False
        )
        await ctx.send(embed=embed)
        await ctx.guild.me.edit(nick=f"[{prefix}] Endroid")

    
    # current prefix command
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.lower().startswith("what is the current prefix") or message.content.lower().startswith("whats the current prefix") or message.content.lower().startswith("what's the current prefix") or message.content.lower().startswith("current prefix"):
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)
                prefix = prefixes[str(message.guild.id)]

            await message.channel.trigger_typing()
            await message.channel.send(f"The current prefix is set to `{prefix}`")


def setup(client):
    client.add_cog(Prefix(client))