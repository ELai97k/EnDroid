import discord
from discord.ext import commands

class Ping(commands.Cog):
    """Bot ping cog."""
    def __init__(self, client):
        self.client = client

    # ping command
    @commands.command(help="Command that shows the bot's latency.")
    async def ping(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.channel.trigger_typing()
        await ctx.send(f"🏓pong! Latency is {round (self.client.latency * 1000)} ms.")
        print("ping pong bot latency revealed")


async def setup(client):
    client.add_cog(Ping(client))