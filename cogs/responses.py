import discord
from discord.ext import commands

class Responses(commands.Cog):
    """Embed for bot's auto-response function."""
    def __init__(self, client):
        self.client = client

    # embed showing bot's auto responses
    @commands.command(help="Embed that shows what messages the bot will auto-respond to.")
    async def responses(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Endroid will automatically respond to the following messages:",
            description = "I'm\nI am\nF\nTell me a joke\n:(\nTell me something\nSay something\nPog\nPoggers\nPogchamp\nPing\nBruh\nHello Endroid\nHi Endroid\nInput\nStupid bot\nDead chat\nTeleport bread\nHey Endroid",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Responses(client))