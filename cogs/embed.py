import discord
from discord.ext import commands

class Embed(commands.Cog):
    """This is a test embed."""
    def __init__(self, client):
        self.client = client

    # test embed
    @commands.command(help="Command for a test embed.")
    async def embed(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Hello world",
            description = "This is a test embed",
            color=0xc7ecf7
        )
        embed.set_footer(text="Thanks for reading")
        await ctx.send(embed=embed)


async def setup(client):
    client.add_cog(Embed(client))