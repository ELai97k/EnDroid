import discord
from discord.ext import commands

class Version(commands.Cog):
    """Displays the Python version for the bot."""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def version(ctx, version):
        version = "python-3.10.7"
        await ctx.send(version)

def setup(client):
    client.add_cog(Version(client))