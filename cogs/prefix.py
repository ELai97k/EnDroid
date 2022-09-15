import discord
import json
from discord.ext import commands

class Prefix(commands.Cog):
    """Cog for the bot's prefixes."""
    def __init__(self, client):
        self.client = client

    # add default prefix and guild id to json file when bot joins server
    @commands.command()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        # default prefix
        prefixes[str(guild.id)] = "!"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    # remove prefix and guild id from json file when bot leaves server
    @commands.command()
    async def on_guild_remove(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    # change prefix command
    @commands.command(help="Command for changing the bot's prefix.")
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

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
            value="?",
            inline=False
        )
        embed.add_field(
            name="New prefix",
            value=f"{prefix}",
            inline=False
        )
        await ctx.send(embed=embed)
        await ctx.guild.me.edit(nick=f"[{prefix}] Endroid")


def setup(client):
    client.add_cog(Prefix(client))