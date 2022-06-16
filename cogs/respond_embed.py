import discord
from discord.ext import commands

class Respond_Embed(commands.Cog):
    def __init__(self, client):
        self.client = client

    # embed showing bot's auto responses
    @commands.command()
    async def responses(self, ctx):
        embed = discord.Embed (
            title = "Endroid will automatically respond to the following messages:",
            description = "`I'm\nI am\nF\nTell me a joke\n:(\nTell me something\nI have no friends\nPog\nPoggers\nPogchamp\nPing\nBruh\nHello Endroid\nHi Endroid\nInput\nStupid bot\nDead chat\nTeleport bread\nHey Endroid`",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Respond_Embed(client))