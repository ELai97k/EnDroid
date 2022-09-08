import discord
from discord.ext import commands

class Version(commands.Cog):
    """Displays the Python version for the bot."""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def version(self, ctx, version):
        version = "Python version: 3.10.7"
        await ctx.send(version)


    @commands.command()
    async def botver(self, ctx):
        embed = discord.Embed (
            title = "Python version",
            description = "```python-3.10.7```",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Version(client))