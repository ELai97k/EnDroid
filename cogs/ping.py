import discord
from discord.ext import commands

class Ping(commands.Cog):
    """Ping command that shows bot latency"""
    def __init__(self, client):
        self.client = client

    # ping command
    @commands.command()
    async def ping(self, ctx):
        if ctx.author == self.client.user:
            return
        await ctx.channel.trigger_typing()
        await ctx.send(f"🏓pong! Latency is {round (self.client.latency * 1000)} ms.")
        print("ping pong bot latency revealed")


def setup(client):
    client.add_cog(Ping(client))