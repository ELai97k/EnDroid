import discord
from discord.ext import commands
import json

class Prefix(commands.Cog):
    """Commands for changing bot prefix"""
    def __init__(self, client):
        self.client = client

    # change prefix command
    @commands.command()
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

    
    # current prefix command
    @commands.command()
    async def currentprefix(self, ctx, prefix):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f"The current prefix is {prefix}")


def setup(client):
    client.add_cog(Prefix(client))