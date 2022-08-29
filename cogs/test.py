import discord
from discord.ext import commands

class Test(commands.Cog):
    """This is a test command"""
    def __init__(self, client):
        self.client = client

    # test command
    @commands.command()
    async def test(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.channel.trigger_typing()
        await ctx.send("This is a test command")
        print("This is a test command and it works!")


def setup(client):
    client.add_cog(Test(client))